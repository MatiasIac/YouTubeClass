import { Player } from './player';
import { Configuration } from './configuration';
import { ConnectionHandler } from './connectionHandler';
import { BulletCloner } from './bulletCloner';

class Game {

    constructor() {
        let canvas = document.createElement('canvas');
        canvas.width = Configuration.width;
        canvas.height = Configuration.height;
        document.body.appendChild(canvas);
        this.context = canvas.getContext('2d');

        this.sprites = [];

        for (let i = 0; i < 5; i++) {
            let sprite = new Image();
            sprite.src = `./sprites/plane${i}.png`;
            this.sprites.push(sprite);
        }

        this.bulletCloner = new BulletCloner();

        this.players = {};
        this.gameObjects = [];
        this.lastFrame = 0;
        this.socketHandler = new ConnectionHandler();

        this.mainLoop = this.mainLoop.bind(this);
        this.playerCreationCallback = this.playerCreationCallback.bind(this);
        this.playerMovingCallback = this.playerMovingCallback.bind(this);
        this.socketHandler.onCreatePlayer = this.playerCreationCallback;
        this.socketHandler.onMoving = this.playerMovingCallback;
    }

    playerMovingCallback(data) {
        if (this.players.hasOwnProperty(data.id) === true) {
            this.players[data.id].changeAngleBy = data.direction;
        }
    }

    playerCreationCallback(playerId) {
        let player = new Player();
        
        player.sprite = this.sprites[this.gameObjects.length];
        player.id = playerId;
        player.bulletCloner = this.bulletCloner;

        this.players[playerId] = player;
        this.gameObjects.push(player);
    }

    mainLoop() {
        const thisFrame = new Date().getTime();
        let delta = (thisFrame - this.lastFrame) / 1000;
        this.lastFrame = thisFrame; 

        this.context.fillStyle = "cyan";
        this.context.fillRect(0, 0, Configuration.width, Configuration.height);
        this.context.save();
        
        this.gameObjects.forEach((p) => {
            if (p.update) p.update(delta);
            if (p.draw) p.draw(this.context);
        });

        this.bulletCloner.update();
        this.bulletCloner.draw(this.context);
        
        this.context.restore();

        window.requestAnimFrame(this.mainLoop);
    }

    init() {
        window.requestAnimFrame = (function(){
            return window.requestAnimationFrame    ||
                window.webkitRequestAnimationFrame || 
                window.mozRequestAnimationFrame    || 
                window.oRequestAnimationFrame      || 
                window.msRequestAnimationFrame     || 
                function(callback, element){
                    window.setTimeout(callback, Configuration.fps);
                };
        })();

        window.requestAnimFrame(this.mainLoop);
    }

}

let game = new Game();
game.init();