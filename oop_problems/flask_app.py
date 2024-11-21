class Config:

    SQLALCHEMY_URI = "*************************"
    MONGO_URI = "mongodb://localhost:4005"


from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Advertiser(db.Model):
    __tablename__ = "advertisers"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    contact_email = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f"Advertiser {self.name}"


class Campaign(db.Model):
    __tablename__ = "campaigns"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    budget = db.Column(db.Float, nullable=False)
    advertiser_id = db.Column(db.Integer, db.ForeignKey("advertisers.id"))

    def __repr__(self):
        return f"Campaign {self.name}"


from flask_pymongo import PyMongo

mongo = PyMongo()


class AdAnalytics:
    def __init__(self, campaign_id, impressions, clicks, timestamp):
        self.campaign_id = campaign_id
        self.impressions = impressions
        self.clicks = clicks
        self.timestamp = timestamp

    def to_dict(self):
        return {
            "campaign_id": self.campaign_id,
            "impressions": self.impressions,
            "clicks": self.clicks,
            "timestamp": self.timestamp,
        }


###################### app


from flask import Flask, request, render_template, redirect, url_for, jsonify


app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

mongo.init_app(app)


@app.route("/advertisers", methods=["POST"])
def create_advertiser():
    data = request.form
    new_advertiser = Advertiser(name=data["name"], contact_email=data["contact_email"])
    db.session.add(new_advertiser)
    db.session.commit()
    return redirect(url_for("list_advertisers"))


@app.route("/analytics", methods=["POST"])
def add_analytics():
    data = request.get_json()
    analytics = AdAnalytics(
        campaign_id=data["campaign_id"],
        impressions=data["impressions"],
        clicks=data["clicks"],
        timestamp=datetime.utcnow(),
    )
    mongo.db.analytics.insert_one(analytics.to_dict())
    return jsonify({"message": "Analytics data added successfully"}), 201


@app.route("/analytics/<campaign_id>", methods=["GET"])
def get_analytics(campaign_id):
    analytics = mongo.db.analytics.find({"campaign_id": campaign_id})
    result = [a for a in analytics]
    for a in result:
        a["_id"] = str(a["_id"])  # Convert ObjectId to string
    return jsonify({"analytics": result}), 200
