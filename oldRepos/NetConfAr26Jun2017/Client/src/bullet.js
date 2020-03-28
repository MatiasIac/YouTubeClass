import { Configuration } from './configuration';

export class Bullet {

    constructor(x, y, angle, playerId, bulletId) {
        this.x = x;
        this.y = y;
        this.angle = angle;
        this.speed = 2.4;
        this.playerId = playerId;
        this.bulletId = bulletId;
    }

    update() {
        this.x += this.speed * Math.cos(this.angle * Configuration.degreeConst);
        this.y += this.speed * Math.sin(this.angle * Configuration.degreeConst);
        
        if ((this.x < 0 && this.x > Configuration.width) ||
            (this.y < 0 && this.y > Configuration.height)) {
            this.destroy();
        }
    }

    draw(context) {
        context.save();
        context.beginPath();
        context.arc(this.x, this.y, 3, 0, 2 * Math.PI, false);
        context.fillStyle = 'rgba(255,0,0,1)';
        context.fill();
        context.closePath();
        context.restore();
    }

}