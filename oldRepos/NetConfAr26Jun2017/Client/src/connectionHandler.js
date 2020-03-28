export class ConnectionHandler {

    constructor() {
        let socket = io();
        
        this._onCreate = this._onCreate.bind(this);
        this._onMoving = this._onMoving.bind(this);
        socket.on("create", this._onCreate);
        socket.on("move", this._onMoving);
    }

    onCreatePlayer() { }

    onMoving() { }

    _onMoving(data) {
        this.onMoving(data);
    }

    _onCreate(data) {
        this.onCreatePlayer(data);
    }

}