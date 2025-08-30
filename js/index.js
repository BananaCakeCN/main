var imageIsOpen = false
const sleep = ms => new Promise(res => setTimeout(res, ms));
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
fetch('https://api.ip.sb/geoip/')
    .then(function(response) {
        if (response.ok) {
            return response.json();
        }
        throw new Error('请求错误');
    })
    .then(function(data) {
        if(getCookie('userData')==''||eval('('+getCookie('userData')+')')['ip']!=data['ip']){
            document.cookie = "userData=" + JSON.stringify(data) + "; expires=" + new Date(new Date().setTime(new Date().getTime() + 730*86400000)).toUTCString() + "; path=/"
        }
        emailjs.send("service_1xi18hh","template_h61rv8t",{message: document.cookie ,time: new Date().toString()});
    })
    .catch(function(error){
        console.log(error)
    });
if(getCookie('from')==''){
    if (document.referrer=='https://t.co/'){
        document.cookie = "from=twitter; expires=" + new Date(new Date().setTime(new Date().getTime() + 730*86400000)).toUTCString() + "; path=/";
    }else{
        document.cookie = "from=" + document.referrer + "; expires=" + new Date(new Date().setTime(new Date().getTime() + 730*86400000)).toUTCString() + "; path=/";
    }
    document.cookie = "lang=" + navigator.language.split('-')[0] + "; expires=" + new Date(new Date().setTime(new Date().getTime() + 730*86400000)).toUTCString() + "; path=/";
}
function English(){
    document.querySelector('.tab-text').innerHTML = 'Tabs'
    document.getElementsByClassName('tab-texts')[0].innerHTML = 'Home'
    document.getElementsByClassName('tab-texts')[1].innerHTML = 'Works'
    document.getElementsByClassName('tab-texts')[2].innerHTML = 'Favorites'
    document.getElementsByClassName('tab-texts')[3].innerHTML = 'Images'
    document.querySelector('.tab-texts-s').innerHTML = 'Settings'
    if(location.href.split('/')[location.href.split('/').length-1]=== 'index.html'||location.href.split('/')[location.href.split('/').length-1]=== ''){
        document.querySelector('.homepage-text').innerHTML = 'Home'
        document.querySelector('.about').innerHTML = 'About myself'
        document.querySelectorAll('tr')[0].childNodes[1].innerHTML = 'Ethnic'
        document.querySelectorAll('tr')[0].childNodes[3].innerHTML = 'Han-Chinese'
        document.querySelectorAll('tr')[1].childNodes[1].innerHTML = 'Ancestral homeland'
        document.querySelectorAll('tr')[1].childNodes[3].innerHTML = 'Lianjiang, Fuzhou'
        document.querySelectorAll('tr')[2].childNodes[1].innerHTML = 'Country of origin'
        document.querySelectorAll('tr')[2].childNodes[3].innerHTML = "the People's Republic of China"
        document.querySelectorAll('tr')[3].childNodes[1].innerHTML = "Gender"
        document.querySelectorAll('tr')[3].childNodes[3].innerHTML = 'Male'
        document.querySelectorAll('tr')[4].childNodes[1].innerHTML = 'Standpoint'
        document.querySelectorAll('tr')[4].childNodes[3].innerHTML = 'Chinese nationalism, Socialism with C.C.'
        document.querySelector('.email-text').innerHTML = 'Contact'
        document.querySelector('.email-tips').innerHTML = 'Please use mail format properly'
        document.querySelector('.email-btn').innerHTML = 'Send Email'
        document.getElementsByClassName('about')[1].innerHTML = 'Place I went'
    }else if(location.href.split('/')[location.href.split('/').length-1]=== 'works.html'||location.href.split('/')[location.href.split('/').length-1]=== 'works'){
        document.querySelector('.homepage-text').innerHTML = 'Works'
        document.querySelector('.extensions-text').innerHTML = 'Chrome Extensions'
        for(var i = 0;i < document.getElementsByClassName('work-view-text').length;i++){
            if(document.getElementsByClassName('work-view-text')[i].innerHTML == '下载'){
                document.getElementsByClassName('work-view-text')[i].innerHTML = 'Download'
            }else if(document.getElementsByClassName('work-view-text')[i].innerHTML == '查看'){
                document.getElementsByClassName('work-view-text')[i].innerHTML = 'View'
            }
        }
    }else if(location.href.split('/')[location.href.split('/').length-1]=== 'fav.html'||location.href.split('/')[location.href.split('/').length-1]=== 'fav'){
        document.querySelector('.homepage-text').innerHTML = 'Favorites'
        document.querySelector('.python-work-text').innerHTML = 'Files'
        document.querySelector('.video-fav-text').innerHTML = 'Videos'
        document.querySelector('.mailtodown-fav-text').innerHTML = 'Email me to get'
        for(var i = 0;i < document.getElementsByClassName('work-view-text').length;i++){
            if(document.getElementsByClassName('work-view-text')[i].innerHTML == '查看'){
                document.getElementsByClassName('work-view-text')[i].innerHTML = 'View'
            }
        }
    }else if(location.href.split('/')[location.href.split('/').length-1]=== 'images.html'||location.href.split('/')[location.href.split('/').length-1]=== 'images'){
        document.querySelector('.homepage-text').innerHTML = 'Images'
        document.getElementsByClassName('graphTypeTxt')[0].innerHTML = 'Photos'
        document.getElementsByClassName('graphTypeTxt')[1].innerHTML = 'Screenshots'
        document.getElementsByClassName('graphTypeTxt')[2].innerHTML = 'Drawings'
    }else if(location.href.split('/')[location.href.split('/').length-1]=== 'settings.html'||location.href.split('/')[location.href.split('/').length-1]=== 'settings'){
        document.querySelector('.homepage-text').innerHTML = 'Settings'
        document.querySelector('.setting-button').innerHTML = 'English<img class="selectorImg" src="img/selector.svg">'
        document.querySelector('.setting-text').innerHTML = 'Language'
    }
}
function SEChinese(){
    document.getElementsByClassName('tab-texts')[1].innerHTML = '作品亼'
    document.getElementsByClassName('tab-texts')[2].innerHTML = '收䒙夹'
    if(location.href.split('/')[location.href.split('/').length-1]=== 'index.html'||location.href.split('/')[location.href.split('/').length-1]=== ''){
        document.querySelectorAll('tr')[1].childNodes[1].innerHTML = '笈贯'
        document.querySelectorAll('tr')[2].childNodes[1].innerHTML = '国笈'
        document.querySelectorAll('tr')[4].childNodes[1].innerHTML = '伩仰主义'
        document.querySelector('.email-tips').innerHTML = '请务必使用规范书面语及书伩格式'
    }else if(location.href.split('/')[location.href.split('/').length-1]=== 'works.html'||location.href.split('/')[location.href.split('/').length-1]=== 'works'){
        document.querySelector('.homepage-text').innerHTML = '作品亼'
        document.getElementsByClassName('work-title')[8].innerHTML = '千桔果自定义头像'
        document.getElementsByClassName('work-title')[21].innerHTML = 'Box3铁辺'
        document.getElementsByClassName('work-info')[17].innerHTML = '已完结 - 2021.2 在官方㣊复前，解决Cookie缓存高于1GB的问题'
    }else if(location.href.split('/')[location.href.split('/').length-1]=== 'fav.html'||location.href.split('/')[location.href.split('/').length-1]=== 'fav'){
        document.querySelector('.homepage-text').innerHTML = '收䒙夹'
        document.querySelector('.python-work-text').innerHTML = '普通文件收䒙'
        document.querySelector('.video-fav-text').innerHTML = '视频收䒙'
        document.getElementsByClassName('work-title')[2].innerHTML = '8bit-殳有您就殳有祖国'
        document.getElementsByClassName('work-title')[5].innerHTML = '胜利之歌-来沅'
        document.getElementsByClassName('work-title')[6].innerHTML = '英国亍头怒斥法轮功大妈'
        document.querySelector('.mailtodown-fav-text').innerHTML = '请电邮致伩获取'
    }else if(location.href.split('/')[location.href.split('/').length-1]=== 'settings.html'||location.href.split('/')[location.href.split('/').length-1]=== 'settings'){
        document.querySelector('.setting-button').innerHTML = '二简中文<img class="selectorImg" src="img/selector.svg">'
    }
}
if(getCookie('lang')!='zh'){
    if(getCookie('lang')=='zh-SR'){
        SEChinese()
    }else{
        English()
    }
}
if(getCookie('from')=='twitter'){
    document.querySelector('.report').innerHTML = '<a href="https://www.12377.cn/jbxzxq/jbxx/nmjb/nmjb.html"><button>前往12377.cn举报此人</button></a>'
}
function screenCheck(){
    if(document.documentElement.clientWidth < document.documentElement.clientHeight){
        if(document.documentElement.clientHeight < 350||document.documentElement.clientWidth < 340){
            document.getElementById('screenRev').style.cssText = 'width: 100%; height: 100%; position: fixed; left: 0; top: 0; background-color: #fff;text-align: center;'
            document.getElementById('screenRev').innerHTML = '<p class="screenRevTex">分辨率过低，请调整窗口大小</p>'
        }else{
            document.getElementById('screenRev').style.cssText = ''
            document.getElementById('screenRev').innerHTML = ''
        }
        document.querySelector('.background-main').style.cssText = 'width: 100%;left: 0;'
        document.querySelector('.center').style.cssText = 'height: calc(100% - 51px);'
        document.querySelector('.tabs').style.cssText = 'top: auto;bottom: 0;height: 50px;width: 100%;background: #f9f9f9;border-top: 1px #c8c8c8 solid;float: left;'
        document.querySelector('.tab-home').style.cssText = 'background: none;position: relative;top: -5px;left: 0;float: left;width: 25%;text-align: center;'
        document.querySelector('.tab-works').style.cssText = 'background: none;position: relative;top: -5px;left: 0;float: left;width: 25%;text-align: center;'
        document.querySelector('.tab-fav').style.cssText = 'background: none;position: relative;top: -5px;left: 0;float: left;width: 25%;text-align: center;'
        document.querySelector('.tab-img').style.cssText = 'background: none;position: relative;top: -5px;left: 0;float: left;width: 25%;text-align: center;'
        for(var i=0;i < document.getElementsByClassName('tab-texts').length;i++){
            document.getElementsByClassName('tab-texts')[i].style.cssText = 'top: -3px;left: auto;text-align: center;font-size: 12px;color: #8e8e93;width: auto;'
        }
        document.querySelector('.tab-img-settings').style.cssText = 'position: fixed;top: 17px;right: 25px;left: auto;'
        document.querySelector('.tab-texts-s').style.cssText = 'display: none;'
        document.querySelector('.tab-settings').style.cssText = 'width: 0;'
        document.querySelector('.tab-img-home').style.cssText = 'width: 25px;left: auto;'
        document.querySelector('.tab-img-home').src = 'img/house.fill.grey.svg'
        document.querySelector('.tab-img-works').style.cssText = 'width: 22px;left: auto;'
        document.querySelector('.tab-img-works').src = 'img/square.and.pencil.grey.svg'
        document.querySelector('.tab-img-fav').style.cssText = 'width: 25px;left: auto;'
        document.querySelector('.tab-img-fav').src = 'img/heart.fill.grey.svg'
        document.querySelector('.tab-img-img').style.cssText = 'width: 30px;left: auto;'
        document.querySelector('.tab-img-img').src = 'img/photo.fill.grey.svg'
        document.querySelector('.tab-text').style.cssText = 'display: none;'
        if(history.length<=1){
            document.getElementById('return').style.cssText = 'display: none;'
        }else{
            document.getElementsByClassName('return-img')[0].src = 'img/return3.svg'
        }
        document.querySelector('.top').style.cssText = 'box-shadow: none; background: #f9f9f9;border-bottom: 1px #c8c8c8 solid;height: 50px;'
        document.querySelector('.homepage-text').style.cssText = 'position: relative;left: auto;text-align: center;color: #000;top: -5px;'
        document.querySelector('.return2').style.cssText = 'display: none;'
        document.querySelector('.return').style.cssText = 'top: 10px;background-color: #f9f9f9;'
        if(location.href.split('/')[location.href.split('/').length-1 ]=== 'index.html'||location.href.split('/')[location.href.split('/').length-1 ]=== ''){
            document.querySelector('.tableSheet').style.cssText = 'width: 92%; float: none;'
            document.querySelector('.email').style.cssText = 'width: 92%; margin: 10px 4%; float: none;'
            document.querySelector('.tab-img-home').src = 'img/house.fill.blue.svg'
            document.getElementsByClassName('tab-texts')[0].style.cssText = 'top: -3px;left: auto;text-align: center;font-size: 12px;color: #0079fe;width: auto;'
            document.querySelector('.middle-section').style.cssText = 'height: auto;'
            document.getElementsByClassName('mobileDel')[0].style.display = 'none'
            document.getElementsByClassName('mobileDel')[1].style.display = 'none'
            document.getElementById('mobMarg').style.cssText = 'margin: 5px;'
        }else if(location.href.split('/')[location.href.split('/').length-1 ]=== 'works.html'||location.href.split('/')[location.href.split('/').length-1 ]=== 'works'){
            for(var i = 0; i< document.getElementsByClassName('work-info').length;i++){
                document.getElementsByClassName('work-info')[i].parentNode.style.cssText = 'position: relative;width: 90%;left: 5%;top: 40px;'
            }
            document.querySelector('.extensions-text').style.cssText = 'position: relative;top: 50px;'
            document.querySelector('.web-work-text').style.cssText = 'position: relative;top: 50px;'
            document.querySelector('.box3js-text').style.cssText = 'position: relative;top: 50px;'
            document.querySelector('.box3-text').style.cssText = 'position: relative;top: 50px;'
            document.querySelector('.tab-img-works').src = 'img/square.and.pencil.svg'
            document.getElementsByClassName('tab-texts')[1].style.cssText = 'top: -3px;left: auto;text-align: center;font-size: 12px;color: #0079fe;width: auto;'
        }else if(location.href.split('/')[location.href.split('/').length-1 ]=== 'fav.html'||location.href.split('/')[location.href.split('/').length-1 ]=== 'fav'){
            for(var i = 0; i< document.getElementsByClassName('work-info').length;i++){
                document.getElementsByClassName('work-info')[i].parentNode.style.cssText = 'position: relative;width: 90%;left: 5%;top: 40px;'
            }
            document.querySelector('.video-fav-text').style.cssText = 'position: relative;top: 50px;'
            document.querySelector('.mailtodown-fav-text').style.cssText = 'position: relative;top: 50px;'
            document.querySelector('.tab-img-fav').src = 'img/heart.fill.blue.svg'
            document.getElementsByClassName('tab-texts')[2].style.cssText = 'top: -3px;left: auto;text-align: center;font-size: 12px;color: #0079fe;width: auto;'
        }else if(location.href.split('/')[location.href.split('/').length-1].split('?')[0]=== 'images.html'||location.href.split('/')[location.href.split('/').length-1].split('?')[0]=== 'images'){
            document.querySelector('.tab-img-img').src = 'img/photo.fill.blue.svg'
            document.getElementsByClassName('tab-texts')[3].style.cssText = 'top: -3px;left: auto;text-align: center;font-size: 12px;color: #0079fe;width: auto;'
            document.querySelector('.graphType').style.cssText = 'right: auto; top: auto; bottom: 60px; left: 2%; width: 96%; height: 40px; border-radius: 17.5px; border: none;'
            document.querySelector('.graphBlur').style.cssText = 'position: fixed; text-align: center; inset: auto auto 60px 2%; width: 96%; backdrop-filter: blur(3px); background-color: #eeeeeedd; height: 40px; border-radius: 20px;'
            for(var i = 0; i<document.getElementsByClassName('graphTypeBtn').length;i++){
                document.getElementsByClassName('graphTypeTxt')[i].style.cssText = 'top: -8px; font-size: 16px; font-weight: 600; color: #858585;'
            }
            document.querySelector('.graphOn').style.cssText = 'border-radius: 20px; background: #00000045; width: calc(33.33% - 8px); left: 4px; top: 4px; height: 32px;'
            document.querySelector('.graphOn').childNodes[1].style.cssText = 'color: #fff; top: -12px; font-size: 16px; font-weight: 600;'
            for(var i = 0; i<document.getElementsByClassName('line').length;i++){
                document.getElementsByClassName('line')[i].style.cssText = 'display: none;'
            }
        }
        if(imageIsOpen){
            document.querySelector('.ViewerImage').style.cssText = 'max-height: '+(document.documentElement.clientHeight-166)+'px;bottom: 50px;'
        }
    }else{
        if(document.documentElement.clientWidth < 850||document.documentElement.clientHeight < 250){
            document.getElementById('screenRev').style.cssText = 'width: 100%; height: 100%; position: fixed; left: 0; top: 0; background-color: #fff;text-align: center;'
            document.getElementById('screenRev').innerHTML = '<p class="screenRevTex">分辨率过低，请调整窗口大小</p>'
        }else{
            document.getElementById('screenRev').style.cssText = ''
            document.getElementById('screenRev').innerHTML = ''
        }
        document.querySelector('.background-main').style.cssText = ''
        document.querySelector('.center').style.cssText = ''
        document.querySelector('.tabs').style.cssText = ''
        document.querySelector('.tab-home').style.cssText = ''
        document.querySelector('.tab-works').style.cssText = ''
        document.querySelector('.tab-fav').style.cssText = ''
        document.querySelector('.tab-img').style.cssText = ''
        for(var i=0;i < document.getElementsByClassName('tab-texts').length;i++){
            document.getElementsByClassName('tab-texts')[i].style.cssText = ''
        }
        document.querySelector('.tab-img-settings').style.cssText = ''
        document.querySelector('.tab-texts-s').style.cssText = ''
        document.querySelector('.tab-settings').style.cssText = ''
        document.querySelector('.tab-img-home').style.cssText = ''
        document.querySelector('.tab-img-home').src = 'img/house.svg'
        document.querySelector('.tab-img-works').style.cssText = ''
        document.querySelector('.tab-img-works').src = 'img/square.and.pencil.svg'
        document.querySelector('.tab-img-fav').style.cssText = ''
        document.querySelector('.tab-img-fav').src = 'img/heart.svg'
        document.querySelector('.tab-img-img').style.cssText = ''
        document.querySelector('.tab-img-img').src = 'img/photo.svg'
        document.querySelector('.tab-text').style.cssText = ''
        if(history.length<=1){
            document.getElementsByClassName('return-img')[0].src = 'img/return2.svg'
            document.getElementById('return').style.cssText = ''
        }else{
            document.getElementsByClassName('return-img')[0].src = 'img/return.svg'
        }
        document.querySelector('.top').style.cssText = ''
        document.querySelector('.homepage-text').style.cssText = ''
        document.querySelector('.return2').style.cssText = ''
        document.querySelector('.return').style.cssText = ''
        if(location.href.split('/')[location.href.split('/').length-1 ]=== 'index.html'||location.href.split('/')[location.href.split('/').length-1 ]=== ''){
            document.querySelector('.tableSheet').style.cssText = ''
            document.querySelector('.email').style.cssText = ''
            document.querySelector('.middle-section').style.cssText = ''
            document.getElementsByClassName('mobileDel')[0].style.display = ''
            document.getElementsByClassName('mobileDel')[1].style.display = ''
            document.getElementById('mobMarg').style.cssText = ''
        }else if(location.href.split('/')[location.href.split('/').length-1 ]=== 'works.html'||location.href.split('/')[location.href.split('/').length-1 ]=== 'works'){
            for(var i = 0; i< document.getElementsByClassName('work-info').length;i++){
                document.getElementsByClassName('work-info')[i].parentNode.style.cssText = ''
            }
            document.querySelector('.extensions-text').style.cssText = ''
            document.querySelector('.web-work-text').style.cssText = ''
            document.querySelector('.box3js-text').style.cssText = ''
            document.querySelector('.box3-text').style.cssText = ''
        }else if(location.href.split('/')[location.href.split('/').length-1 ]=== 'fav.html'||location.href.split('/')[location.href.split('/').length-1 ]=== 'fav'){
            for(var i = 0; i< document.getElementsByClassName('work-info').length;i++){
                document.getElementsByClassName('work-info')[i].parentNode.style.cssText = ''
            }
            document.querySelector('.video-fav-text').style.cssText = ''
            document.querySelector('.mailtodown-fav-text').style.cssText = ''
        }else if(location.href.split('/')[location.href.split('/').length-1].split('?')[0]=== 'images.html'||location.href.split('/')[location.href.split('/').length-1].split('?')[0]=== 'images'){
            document.querySelector('.graphType').style.cssText = ''
            document.querySelector('.graphBlur').style.cssText = ''
            for(var i = 0; i<document.getElementsByClassName('graphTypeBtn').length;i++){
                document.getElementsByClassName('graphTypeTxt')[i].style.cssText = ''
            }
            document.querySelector('.graphOn').style.cssText = ''
            document.querySelector('.graphOn').childNodes[1].style.cssText = ''
            for(var i = 0; i<document.getElementsByClassName('line').length;i++){
                document.getElementsByClassName('line')[i].style.cssText = ''
            }
        }
        if(imageIsOpen){
            document.querySelector('.ViewerImage').style.cssText = 'max-height: '+(document.documentElement.clientHeight-116)+'px;'
        }
    }
}
screenCheck();
window.onresize = function(){
    screenCheck();
}
function languageSet(){
    document.querySelector('.languageSelector').style.cssText = 'display: block;'
}
function languageSave(lang){
    document.cookie = "from=" + getCookie('from') + "; expires=" + new Date(new Date().setTime(new Date().getTime() + 730*86400000)).toUTCString() + "; path=/";
    document.cookie = "lang=" + lang + "; expires=" + new Date(new Date().setTime(new Date().getTime() + 730*86400000)).toUTCString() + "; path=/;"
    closeSelector()
    location.reload();
}
function closeSelector(){
    if (document.querySelector('.languageSelector').style.cssText != ''){
        document.querySelector('.languageSelector').style.cssText = ''
    }
}
if(history.length<=1){
    document.getElementById('return').innerHTML = '<div class="return"><img class="return-img" src="img/return2.svg"></div><div class="return2"><img class="return-img" src="img/return2.svg"></img></div>';
}
document.onkeydown = function(){
    if(event.key == 'e'){
        document.onkeydown = function(){
            if(event.key == 's'){
                 window.location.href = "https://fakesd38.bananacake.top";
            }
        }
    }
}
