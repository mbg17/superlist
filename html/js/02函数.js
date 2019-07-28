// 立即执行函数
(function (a,b) {
    console.log(a,b);
})(1,2);
// 标准函数
function add(a,b) {
    return a+b;
}
// 匿名函数
foo = function (a,b){
    return a+b;
};
console.log(foo(100,200));
console.log(add(300,400));
// 编写代码，将当前日期按“2017-12-27 11:11 星期三”格式输出。
var day ={0:'七',1:'一',2:'二',3:'三',4:'四',5:'五',6:'六'}
console.log(date.getFullYear().toString() + '-'
    + date.getMonth().toString() + '-' + date.getDate().toString()
    + ' ' + date.getHours().toString() + ':'
    + date.getMinutes().toString() + ' 星期' + day[date.getDay()]);