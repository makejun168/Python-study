// 练习
// 修一个游泳池 半径(以米为单位)在程序运行时输入 游泳池外修一条3米宽的过道
// 过道的外侧修一圈围墙 已知过道的造价为25元每平米 围墙的造价为32.5元每米
// 输出围墙和过道的总造价分别是多少钱(精确到小数点后2位)

class Circle {
    constructor(props) {
        this.radius = props.radius;
        console.log(this.radius);
    }

    perimeter = () => {
        return 2 * this.radius * Math.PI;
    }

    area = () => {
        return Math.PI * this.radius * this.radius;
    }
}

const smallCircle = new Circle({radius: 5})
const bigCircle = new Circle({radius: 5 + 3})

console.log(smallCircle.perimeter())
console.log(smallCircle.area())
console.log(bigCircle.perimeter())
console.log(bigCircle.area())
console.log(bigCircle.perimeter() * 32.5)
console.log((bigCircle.area() - smallCircle.area()) * 25);
