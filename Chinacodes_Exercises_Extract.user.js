// ==UserScript==
// @name         Chinacodes_Exercises_Extract
// @namespace    https://github.com/Harrison-1eo/Chinacodes_Exercises_Extract
// @version      1.0
// @description  Extract and send page source to a local Python program
// @author       Harrison_1eo
// @match        https://www.chinacodes.com.cn/exercises/gotoExercises.do
// @grant        GM_xmlhttpRequest
// ==/UserScript==

(function() {
    'use strict';

    // 创建一个按钮并添加到网页右上角
    const button = document.createElement('button');
    button.textContent = '提取源码并复制';
    button.style.position = 'fixed';
    button.style.top = '10px';
    button.style.right = '10px';
    document.body.appendChild(button);

    // 添加按钮点击事件监听器
    button.addEventListener('click', function() {
        // 提取当前网页的源码
        const pageSource = document.documentElement.outerHTML;

        // 使用 clipboard.writeText 方法进行复制
        navigator.clipboard.writeText(pageSource)
        .then(() => {
            // 提示用户源码已复制
            alert('网页源码已复制到剪切板！');
        })
        .catch(error => {
            console.error('复制到剪切板时出错:', error);
        });

    });
})();
