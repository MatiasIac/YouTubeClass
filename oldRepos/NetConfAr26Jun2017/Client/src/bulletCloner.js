import { Bullet } from './bullet';

export class BulletCloner {

    constructor() {
        this.bulletRandomPropertyCounter = 0;
        this.bullets = { };
    }

    cloneBullet(x, y, angle, playerId) {
        this.bulletRandomPropertyCounter++;
        let bullet = new Bullet(x, y, angle, playerId, this.bulletRandomPropertyCounter);

        bullet.destroy = () => {
            delete this.bullets[bullet.bulletId];
        };

        this.bullets[this.bulletRandomPropertyCounter] = bullet;
    }

    update() {
        for (var p in this.bullets) {
            this.bullets[p].update();
        }
    }

    draw(context) {
        for (var p in this.bullets) {
            this.bullets[p].draw(context);
        }
    }

}