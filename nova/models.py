from nova import db


class Game(db.Model):
    gameId = db.Column(db.Integer, primary_key=True, autoincrement=True)
    timeCompression = db.Column(db.Float, default=1)
    lastActionTime = db.Column(db.DateTime)
    eventCounter = db.Column(db.Integer, default=0)
    startTime = db.Column(db.DateTime, nullable=False)
    endTime = db.Column(db.DateTime, nullable=False)
    deathProbeCost = db.Column(db.Integer, default=200)
    spyProbeCost = db.Column(db.Integer, default=10)
    factoryCost = db.Column(db.Integer, default=5)
    speedCost = db.Column(db.Integer, default=500)
    battlePowerCost = db.Column(db.Integer, default=100)
    rangeCost = db.Column(db.Integer, default=100)
    probeShieldCost = db.Column(db.Integer, default=10)
    deathShieldCost = db.Column(db.Integer, default=200)
    name = db.Column(db.String(255))

    def __repr__(self):
        return f"<Game {self.name}>"


class User(db.Model):
    userId = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f"<User {self.name}>"


class Player(db.Model):
    playerId = db.Column(db.Integer, primary_key=True, autoincrement=True)
    gameId = db.Column(db.Integer, db.ForeignKey("game.gameId"), nullable=False)
    userId = db.Column(db.Integer, db.ForeignKey("user.userId"), nullable=False)
    name = db.Column(db.String(64), nullable=False)
    wealth = db.Column(db.Integer, default=250)
    battlePower = db.Column(db.Integer, default=100)
    range = db.Column(db.Float, default=10)
    speed = db.Column(db.Float, default=0.5)

    def __repr__(self):
        return f"<Player {self.name}>"


class Star(db.Model):
    starId = db.Column(db.Integer, primary_key=True, autoincrement=True)
    gameId = db.Column(db.Integer, db.ForeignKey("game.gameId"), nullable=False)
    name = db.Column(db.String(64), nullable=False)
    x = db.Column(db.Integer, nullable=False)
    y = db.Column(db.Integer, nullable=False)
    wealth = db.Column(db.Integer, default=10)
    numShips = db.Column(db.Integer, default=0)
    numFactories = db.Column(db.Integer, default=0)
    hasSpyShield = db.Column(db.Boolean, default=False)
    hasDeathShield = db.Column(db.Boolean, default=False)
    ownerId = db.Column(db.Integer, db.ForeignKey("player.playerId"))
    homeWorldOfId = db.Column(db.Integer, db.ForeignKey("player.playerId"))
    isDead = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f"<Star {self.name}>"


# Expose the MetaData object
Base = db.Model
metadata = db.Model.metadata
