from flask import Flask, request
from trainer_manager import TrainerManager
from gym_leader import GymLeader
from regular_trainer import RegularTrainer

import json

app = Flask(__name__)

trainer_manager = TrainerManager("./trainer_list.json")


# API Methods
@app.route('/trainermanager/trainers', methods=['POST'])
def add_trainer():
    '''Adds entity JSON to Trainer Manager'''
    pass


@app.route('/trainermanager/trainers/<id>', methods=['PUT'])
def update_trainer():
    '''Update entity JSON in Trainer Manager'''
    pass


@app.route('/trainermanager/trainers/<id>', methods=['DELETE'])
def delete_trainer():
    '''Delete entity JSON in Trainer Manager'''
    pass


@app.route('/trainermanager/trainers/<id>', methods=['GET'])
def get_trainer_by_id():
    '''Get entity JSON by ID in Trainer Manager'''
    pass


@app.route('/trainermanager/trainers/all', methods=['GET'])
def get_all_trainers():
    '''Gets all trainers'''
    pass


@app.route('/trainermanager/trainers/all/<type>', methods=['GET'])
def get_all_trainers_by_type():
    '''Gets all trainers by type'''
    pass


@app.route('/trainermanager/trainers/stats', methods=['GET'])
def get_stats():
    '''Get stats for trainer manager'''
    pass
