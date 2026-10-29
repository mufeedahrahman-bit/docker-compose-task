
from flask import Flask, jsonify
import os
import redis

app = Flask(__name__)

redis_client = redis.Redis(
    host=os.getenv("REDIS_HOST", "redis"),
    port=int(os.getenv("REDIS_PORT", "6379")),
    decode_responses=True
)

@app.route("/")
def home():
    visits = redis_client.incr("visits")
    return jsonify(
        message="Docker Compose application is running!",
        visit_count=visits
    )

@app.route("/health")
def health():
    redis_client.ping()
    return jsonify(status="healthy", redis="connected")
