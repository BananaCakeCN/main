function getCreateDay(){
    return Math.floor((new Date(new Date().toLocaleString("zh-CN", {timeZone: "America/Chicago"})).getTime()-new Date("2022-04-09T08:00:20.000+08:00").getTime())/1000/(3600*24))
}
function getDomainDay(){
    return Math.floor((new Date(new Date().toUTCString()).getTime()-new Date("2023-09-26 06:20:23").getTime())/1000/(3600*24))
}
const element = document.getElementsByClassName('websiteTime')[0]
element.innerHTML = '页面已运行 ' + getCreateDay() + ' 日，域名 "bananacake.top" 已注册 ' + getDomainDay() + ' 日'
