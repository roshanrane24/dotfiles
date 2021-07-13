package main

import (
	"encoding/json"
	"flag"
	"fmt"
	"io"
	"io/fs"
	"io/ioutil"
	"math"
	"net/http"
	"os"
	"path"
	"strconv"
	"strings"
	"time"
)


var (
    unit = flag.String("unit", "standard", "unit to use ([standard] | metric | imperial)")
)

var (
    apikey string
    location string
    url string
    err error
    apiData WeatherData
    files []fs.FileInfo
)

type WeatherData struct {
    Coord coord `json:"coord"`
    Weather []weather `json:"weather"`
    Base string `json:"base"`
    Main conditions `json:"main"`
    Visibility int `json:"visibility"`
    Wind wind `json:"wind"`
    Clouds clouds `json:"clouds"`
    Dt int `json:"dt"`
    Sys sys `json:"sys"`
    Timezone int `json:"timezone"`
    Id int `json:"id"`
    Name string `json:"name"`
    Cod int `json:"cod"`
}

type coord struct {
    Longitude float32 `json:"lon"`
    Latitude float32 `json:"lat"`
}

type weather struct {
    Id int `json:"id"`
    Main string `json:"main"`
    Description string `json:"description"`
    Icon string `json:"icon"`
}

type conditions struct {
    Temp float64 `json:"temp"`
    FeelsLike float64 `json:"feels_like"`
    TempMin float64 `json:"temp_min"`
    TempMax float64 `json:"temp_max"`
    Pressure int `json:"pressure"`
    Humidity int `json:"humidity"`
    SeaLevel int `json:"sea_level"`
    GroundLevel int `json:"grnd_level"`
}

type wind struct {
    Speed float32 `json:"speed"`
    Deg int `json:"deg"`
    Gust float32 `json:"gust"`
}

type clouds struct {
    All int `json:"all"`
}

type sys struct {
    Type int `json:"type"`
    Id int `json:"id"`
    Country string `json:"country"`
    Sunrise int `json:"sunrise"`
    Sunset int `json:"sunset"`
}

func main() {
    flag.Parse()

    apikey := "YOURAPIKEY"
    location := "LOCATION"

    switch *unit {
    case "metric":
        url = "https://api.openweathermap.org/data/2.5/" +
                          "weather?q=" + location + "&units=metric" +
                          "&appid=" + apikey
    case "imperial":
        url = "https://api.openweathermap.org/data/2.5/" +
                          "weather?q=" + location + "&units=imperial" +
                          "&appid=" + apikey
    default:
        url = "https://api.openweathermap.org/data/2.5/" +
                          "weather?q=" + location + "&appid=" + apikey
        }

    check()
    files, _ = ioutil.ReadDir(path.Join(os.Getenv("HOME"), ".cache/eww-weather"))
    if len(files) < 1 {
        status := getResponseData(url)
        if status != 200 {
            fmt.Print(status)
            os.Exit(0)
        }
        cacheData()
        files, _ = ioutil.ReadDir(path.Join(os.Getenv("HOME"), ".cache/eww-weather"))
    }
    file, _ := strconv.ParseInt(files[0].Name(), 10, 64)
    fileTime := time.Unix(file, 0)

    if time.Now().Before(fileTime.Add(time.Duration(10)*time.Minute)) {
        getCachedData()
    } else {
        status := getResponseData(url)
        if status != 200 {
            fmt.Print(status)
            os.Exit(0)
        }
        cacheData()
    }
    switch flag.Arg(0) {
    case "temp":
        fmt.Print(math.Round(apiData.Main.Temp))
    case "actual":
        fmt.Print(math.Round(apiData.Main.FeelsLike))
    case "pressure":
        fmt.Print(apiData.Main.Pressure)
    case "humidity":
        fmt.Print(apiData.Main.Humidity)
    case "description":
        fmt.Print(strings.Title(apiData.Weather[0].Description))
    case "wind-speed":
        fmt.Print(apiData.Wind.Speed)
    case "wind-direction":
        fmt.Print(apiData.Wind.Deg)
    case "location":
        fmt.Print(strings.Title(apiData.Name))
    case "icon":
        getIcon()
        fmt.Print("resources/" + apiData.Weather[0].Icon + ".png")
    default:
        fmt.Print("Err")
    }

}


func check()  {
    cachePath := path.Join(os.Getenv("HOME"), ".cache/eww-weather")
    _, err = os.Stat(cachePath)
    if os.IsNotExist(err) {
        err = os.Mkdir(cachePath, 0755)
        out, _ := os.Create(path.Join(cachePath, fmt.Sprint(time.Now().Add(time.Duration(-1)*time.Hour).Unix())))
        defer out.Close()
    }

    resDir := path.Join(os.Getenv("HOME"), ".config/eww/resources")
    _, err = os.Stat(resDir)
    if os.IsNotExist(err) {
        err = os.Mkdir(resDir, 0755)
    }
}


func getResponseData(url string) int {
    resp, err := http.Get(url)
    if err != nil {
        return resp.StatusCode
    }
    defer resp.Body.Close()

    respData, err := ioutil.ReadAll(resp.Body)
    if err != nil {
        return 1
    }

    json.Unmarshal(respData, &apiData)

    return resp.StatusCode
}


func cacheData()  {
    data, err := json.Marshal(&apiData)
    if err != nil {
        return
    }
    files, err := ioutil.ReadDir(path.Join(os.Getenv("HOME"), ".cache/eww-weather"))
    if len(files) > 0 {
        os.Remove(path.Join(os.Getenv("HOME"), ".cache/eww-weather", files[0].Name()))
    }
    file, err := os.Create(path.Join(os.Getenv("HOME"), ".cache/eww-weather", strconv.FormatInt(time.Now().Unix(), 10)))
    if err != nil {
        return
    }
    defer file.Close()
    file.Write(data)
}


func getCachedData()  {
    files, _ := ioutil.ReadDir(path.Join(os.Getenv("HOME"), ".cache/eww-weather"))
    data, _ := ioutil.ReadFile(path.Join(os.Getenv("HOME"), ".cache/eww-weather", files[0].Name()))
    json.Unmarshal(data, &apiData)
}


func getIcon()  {

    icon, err := http.Get("http://openweathermap.org/img/wn/" + apiData.Weather[0].Icon + "@2x.png")
    if err != nil {
        return
    }
    defer icon.Body.Close()

    file, _ := os.Create(path.Join(os.Getenv("HOME"), ".config/eww/resources", apiData.Weather[0].Icon + ".png"))

    defer file.Close()
    io.Copy(file, icon.Body)
}
