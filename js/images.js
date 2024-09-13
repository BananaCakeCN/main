function getCookie(cname){
    var name = cname + "=";
    var decodedCookie = decodeURIComponent(document.cookie);
    var ca = decodedCookie.split(';');
    for(var i = 0; i <ca.length; i++) {
        var c = ca[i];
        while (c.charAt(0) == ' ') {
            c = c.substring(1);
         }
         if (c.indexOf(name) == 0) {
            return c.substring(name.length, c.length);
         }
     }
    return "";
}
function getUrl(root, i){
    if(i > 111 && root == 'photos/'){
        return 'https://assets2.bananacake.top/' + root + i + '.png';
    }
    return 'https://assets.bananacake.top/' + root + i + '.png';
}
async function imageClickOnce(index){
    if(document.documentElement.clientWidth < document.documentElement.clientHeight){
        document.getElementsByClassName('photo')[albumLength-index].style.cssText = 'animation: imageOpen 0.5s forwards;'
        document.getElementsByClassName('photo')[albumLength-index].childNodes[0].style.cssText = ''
        await sleep(500)
        imageIsOpen = true
        document.querySelector('.photoViewer').style.cssText = 'height: 100%;width: 100%;background-color: #FFF;display: flex;'
        document.querySelector('.photoViewer').innerHTML = '<img style="max-height: '+(document.documentElement.clientHeight-116)+'px;" src="'+document.getElementsByClassName('photo')[albumLength-index].childNodes[0].src+'" class="ViewerImage"></img><div class="imageTop"><p class="imageInfo">'+images[document.getElementsByClassName('photo')[albumLength-index].childNodes[0].src.split('/')[document.getElementsByClassName('photo')[albumLength-index].childNodes[0].src.split('/').length-1].split('.')[0]][1]+'</p><p class="imageInfo2">'+images[document.getElementsByClassName('photo')[albumLength-index].childNodes[0].src.split('/')[document.getElementsByClassName('photo')[albumLength-index].childNodes[0].src.split('/').length-1].split('.')[0]][0]+'</p><div class="button1 return imageReturn" onclick="closeImage()"><img class="return-img2" src="img/return.svg"></div></div>'
        document.querySelector('.ViewerImage').style.cssText = 'max-height: '+(document.documentElement.clientHeight-166)+'px;bottom: 50px;'
    }else{
        for (var i = 0;i < document.getElementsByClassName('photo').length; i++){
            if(document.getElementsByClassName('photo')[i].childNodes[0].src.split('/')[document.getElementsByClassName('photo')[0].childNodes[0].src.split('/').length-1]==index+'.png'){
                document.getElementsByClassName('photo')[i].childNodes[0].style.cssText = 'border: 3px #0064e1 solid;border-radius: 3px;padding: 1px;'
            }else{
                document.getElementsByClassName('photo')[i].childNodes[0].style.cssText = ''
            }
        }
    }
}
async function closeImage(){
    imageIsOpen = false
    document.querySelector('.photoViewer').innerHTML = ''
    document.querySelector('.photoViewer').style.cssText = ''
    for(var i = 0; i < document.getElementsByClassName('photo').length; i++){
        if(document.getElementsByClassName('photo')[i].style.cssText != ''){
            document.getElementsByClassName('photo')[i].style.cssText = 'animation: imageClose 0.5s forwards;'
            await sleep(500)
            document.getElementsByClassName('photo')[i].style.cssText = ''
        }
    }
}
function loadMoreImage(){
    displayed2 = displayed-10
    if(displayed2 <= 0){
        displayed2 = 0
        loadMore = ''
    }
    for(var i = displayed; i>displayed2;i--){
        load = load + '<div class="photo" onclick="imageClickOnce('+i+')"><img src="' + getUrl(root, i) + '" class="image"></img></div>'
    }
    document.querySelector('.center').innerHTML = load + loadMore
    for (var i = 0;i < document.getElementsByClassName('photo').length; i++){
        document.getElementsByClassName('photo')[i].ondblclick = async function(){
            this.style.cssText = 'animation: imageOpen 0.5s forwards;'
            this.childNodes[0].style.cssText = ''
            await sleep(500)
            imageIsOpen = true
            document.querySelector('.photoViewer').style.cssText = 'height: 100%;width: 100%;background-color: #FFF;display: flex;'
        document.querySelector('.photoViewer').innerHTML = '<img style="max-height: '+(document.documentElement.clientHeight-116)+'px;" src="'+this.childNodes[0].src+'" class="ViewerImage"></img><div class="imageTop"><p class="imageInfo">'+images[this.childNodes[0].src.split('/')[this.childNodes[0].src.split('/').length-1].split('.')[0]][1]+'</p><p class="imageInfo2">'+images[this.childNodes[0].src.split('/')[this.childNodes[0].src.split('/').length-1].split('.')[0]][0]+'</p><div class="button1 return imageReturn" onclick="closeImage()"><img class="return-img2" src="img/return.svg"></div><div class="button1 imageDetails" onclick="imageDetails(`' + this.childNodes[0].src + '`)"><img class="details-img" src="img/info.circle.svg"></div></div><div id="imgDetails" style="width: 0; height: 0;"></div>';
            if(document.documentElement.clientWidth < document.documentElement.clientHeight){
                document.querySelector('.ViewerImage').style.cssText = 'max-height: '+(document.documentElement.clientHeight-166)+'px;bottom: 50px;'
            }
        }
    }
    displayed -= 10
}
if(new URLSearchParams(window.location.search).get('album')=='photos'||new URLSearchParams(window.location.search).get('album')==null){
    var albumLength = Object.keys(photos).length
    var root = 'photos/'
    var images = photos;
    document.getElementsByClassName('graphTypeBtn')[0].classList.add('graphOn');
    document.getElementsByClassName('graphTypeBtn')[1].className = 'graphTypeBtn';
    document.getElementsByClassName('graphTypeBtn')[2].className = 'graphTypeBtn';
}else if(new URLSearchParams(window.location.search).get('album')=='screenshots'){
    var albumLength = Object.keys(screenshots).length
    var root = 'screenshots/'
    var images = screenshots;
    document.getElementsByClassName('graphTypeBtn')[0].className = 'graphTypeBtn';
    document.getElementsByClassName('graphTypeBtn')[1].classList.add('graphOn');
    document.getElementsByClassName('graphTypeBtn')[2].className = 'graphTypeBtn';
}else if(new URLSearchParams(window.location.search).get('album')=='drawings'){
    var albumLength = Object.keys(drawings).length
    var root = 'drawings/'
    var images = drawings;
    document.getElementsByClassName('graphTypeBtn')[0].className = 'graphTypeBtn';
    document.getElementsByClassName('graphTypeBtn')[1].className = 'graphTypeBtn';
    document.getElementsByClassName('graphTypeBtn')[2].classList.add('graphOn');
}
var load = ''
var displayed = albumLength - Math.ceil((document.documentElement.clientHeight-70)/(document.documentElement.clientWidth*0.85/5))*5
var displayed2
var loadMore
if(displayed < 0){
    displayed = 0
}
for(var i = albumLength; i>displayed;i--){
    if(displayed>0){
        if(getCookie('lang')=='zh-SR'||getCookie('lang')=='zh'){
            loadMore = '<button onclick="loadMoreImage()" class="loadMore">加载更多</button>'
        }else{
            loadMore = '<button onclick="loadMoreImage()" class="loadMore">Load More</button>'
        }
    }else{
        loadMore = ''
    }
    load = load + '<div class="photo" onclick="imageClickOnce('+i+')"><img src="' + getUrl(root, i) + '" class="image"></img></div>'
}
document.querySelector('.center').innerHTML = load + loadMore
for (var i = 0;i < document.getElementsByClassName('photo').length; i++){
    document.getElementsByClassName('photo')[i].ondblclick = async function(){
        this.style.cssText = 'animation: imageOpen 0.5s forwards;'
        this.childNodes[0].style.cssText = ''
        await sleep(500)
        imageIsOpen = true
        document.querySelector('.photoViewer').style.cssText = 'height: 100%;width: 100%;background-color: #FFF;display: flex;'
        document.querySelector('.photoViewer').innerHTML = '<img style="max-height: '+(document.documentElement.clientHeight-116)+'px;" src="'+this.childNodes[0].src+'" class="ViewerImage"></img><div class="imageTop"><p class="imageInfo">'+images[this.childNodes[0].src.split('/')[this.childNodes[0].src.split('/').length-1].split('.')[0]][1]+'</p><p class="imageInfo2">'+images[this.childNodes[0].src.split('/')[this.childNodes[0].src.split('/').length-1].split('.')[0]][0]+'</p><div class="button1 return imageReturn" onclick="closeImage()"><img class="return-img2" src="img/return.svg"></div><div class="button1 imageDetails" onclick="imageDetails(`' + this.childNodes[0].src + '`)"><img class="details-img" src="img/info.circle.svg"></div></div><div id="imgDetails" style="width: 0; height: 0;"></div>';
        if(document.documentElement.clientWidth < document.documentElement.clientHeight){
            document.querySelector('.ViewerImage').style.cssText = 'max-height: '+(document.documentElement.clientHeight-166)+'px;bottom: 50px;'
        }
    }
}
async function imageDetails(url){
    if(document.getElementById('imgDetails').style.cssText == 'width: 0px; height: 0px;'){
        document.getElementById('imgDetails').style.cssText = 'width: 300px; position: absolute; right: 13px; background-color: #fff; border: #e6e6e6 1px solid; border-radius: 7px; top: 113px; padding: 10px; color: #404040;'
        document.getElementById('imgDetails').innerHTML = '<b>设备</b><p>--</p><b>时间</b><p>----年--月--日 --:--:--</p><b>位置（中国大陆不可用）</b><div id="map"></div>'
        document.getElementsByClassName('imageDetails')[0].style.backgroundColor = '#e9e9e8';
        document.getElementsByClassName('details-img')[0].src = 'img/info.circle.fill.svg';
        const tags = await ExifReader.load(url);
        const date = new Date(tags['DateCreated']['value'])
        document.getElementById('imgDetails').innerHTML = '<b>设备</b><p>' + tags['LensModel']['value'] + '</p><b>时间</b><p>' + date.getFullYear() + '年' + (date.getMonth() + 1) + '月' + date.getDate() + '日 ' + date.getHours() + ':' + date.getMinutes() + ':' + date.getSeconds() + '</p><b>位置（中国大陆不可用）</b><div id="map"></div>'
        if(tags['GPSLatitude'] == undefined){
            document.getElementById('map').innerHTML = '<p>照片不包含位置信息，或位置信息已被去除</p>';
        }else{
            var map = L.map('map', {attributionControl: false}).setView([(tags['GPSLatitude']['description'].substring(tags['GPSLatitude']['description'].length - 1) == 'S' ? '-' : '') + tags['GPSLatitude']['description'].substring(0, tags['GPSLatitude']['description'].length - 1), (tags['GPSLongitude']['description'].substring(tags['GPSLongitude']['description'].length - 1) == 'W' ? '-' : '') + tags['GPSLongitude']['description'].substring(0, tags['GPSLongitude']['description'].length - 1)], 13);
            L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', ).addTo(map);
            L.marker([(tags['GPSLatitude']['description'].substring(tags['GPSLatitude']['description'].length - 1) == 'S' ? '-' : '') + tags['GPSLatitude']['description'].substring(0, tags['GPSLatitude']['description'].length - 1), (tags['GPSLongitude']['description'].substring(tags['GPSLongitude']['description'].length - 1) == 'W' ? '-' : '') + tags['GPSLongitude']['description'].substring(0, tags['GPSLongitude']['description'].length - 1)]).addTo(map);
        }
    }else{
        document.getElementById('imgDetails').style.cssText = 'width: 0px; height: 0px;';
        document.getElementById('imgDetails').innerHTML = '';
        document.getElementsByClassName('imageDetails')[0].style.backgroundColor = '';
        document.getElementsByClassName('details-img')[0].src = 'img/info.circle.svg';
    }
}
