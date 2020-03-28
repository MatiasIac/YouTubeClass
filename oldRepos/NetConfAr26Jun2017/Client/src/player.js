import { Configuration } from './configuration';

export class Player {
    
    constructor() {
        this.x = Configuration.width / 2;
        this.y = Configuration.height / 2;
        this.speed = 1.4;
        this.angle = 0;
        this.movingAngleTo = 0;
        this.timeAccumulator = 0;
    }

    set changeAngleBy(v) {
        this.movingAngleTo = parseFloat(v);
    }

    set id(guid) {
        this.GUID = guid;
    }

    set sprite(s) {
        this.sprite_sheet = s;
    }

    set bulletCloner(c) {
        this.bullet_cloner = c;
    }

    checkBounds() {
        if (this.x > Configuration.width) {
            this.x = 1;
        }

        if (this.x < -Configuration.playerSpriteWidth) {
            this.x = Configuration.width - 1;
        }

        if (this.y < -Configuration.playerSpriteHeight) {
            this.y = Configuration.height - 1;
        }

        if (this.y > Configuration.height) {
            this.y = 1;
        }
    }

    update(delta) {
        this.timeAccumulator += delta;
        this.angle += this.movingAngleTo;
        this.x += this.speed * Math.cos(this.angle * Configuration.degreeConst);
        this.y += this.speed * Math.sin(this.angle * Configuration.degreeConst);

        this.checkBounds();

        if (this.timeAccumulator > 1) {
            this.bullet_cloner.cloneBullet(this.x, this.y, this.angle, this.GUID);
            this.timeAccumulator = 0;
        }
    }

    draw(context) {
        context.save();
        context.translate(this.x, this.y);
        context.rotate((this.angle + 90) * Configuration.degreeConst);
        context.translate(-(Configuration.playerSpriteWidth / 2), -(Configuration.playerSpriteHeight / 2));
        context.drawImage(this.sprite_sheet, 0, 0);
		context.restore();        
    }
}