alert(123)
var ufind;
// 字符串
var s1 = '123';
var s2 = 'luyuan'
var s3 = null;
s2.length;//字符串长度
s2.concat('321')//拼接字段
s2.charAt(2)//返回指定位置的字符串
s2.indexOf('2')//子序列位置
s2.substring(1,2)//返回范围内的字符串（顾头不顾尾）
//end<start end 放到第一位 start<0 自动变成0
s2.slice(1,2)//切片
//trim 去除空格
// 数字
var n1 = 1234;
var n2 = NaN;
//数组
var l1 = [1,2,3,4,5]
// 布尔值
var T = true;
var F = false;
// 数据类型
console.log(typeof s1);
console.log(typeof s2);
console.log(typeof s3);
console.log(typeof n1);
console.log(typeof n2);
console.log(typeof l1);
console.log(typeof T);
console.log(typeof ufind);
// 条件控制
if (s1>n1){
    console.log('s1>n1');
}else if (s1 >100){
    console.log('s1>100');
}else{
    console.log('small');
}
// for 循环
for(var i = 0; i<l1.length;i++){
    console.log(l1[i]);
}
// 运算符
var test =100;
switch (test) {
    case 0:
        console.log(test);
        break;
    case 100:
        console.log(100);
        break;
    default:
        console.log('...')
}
while(n1<=1236){
    console.log('不大于1236');
    n1++;
}
l1.forEach(console.log,//回调函数
    l1);//当前对象

var sum = 0;
// forEach 把当前值和索引位置传给item和index
[1, 2, 3, 4].forEach(function (item, index, array) {
  console.log(index,item); // true
  sum += item;
});

alert(sum); // 10