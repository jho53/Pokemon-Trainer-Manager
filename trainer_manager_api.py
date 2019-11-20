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
    content = request.json
    try:
        if content['type'] == 'Regular Trainer':
            regular_trainer = RegularTrainer(
                content['name'], content['pokemon_team'],
                content['trainer_class'], content['pokecoins'],
                content['location'], content['movement_type'],
                content['phone_num'], content['have_partner'])
            response = app.response_class(
                response=str(trainer_manager.add(regular_trainer)), status=200)
        elif content['type'] == 'Gym Leader':
            gym_leader = GymLeader(content['name'], content['pokemon_team'],
                                   content['trainer_class'],
                                   content['pokecoins'], content['location'],
                                   content['badge'], content['element'],
                                   content['prize'])
            response = app.response_class(
                response=str(trainer_manager.add(gym_leader)), status=200)
        else:
            response = app.response_class(
                response='Type not supported', status=400)
    except Exception as e:
        response = app.response_class(response=str(e), status=400)
    return response


@app.route('/trainermanager/trainers/<int:trainer_id>', methods=['PUT'])
def update_trainer(trainer_id):
    '''Update entity JSON in Trainer Manager'''
    content = request.json
    try:
        if content['type'] == 'Regular Trainer':
            regular_trainer = RegularTrainer(
                content['name'], content['pokemon_team'],
                content['trainer_class'], content['pokecoins'],
                content['location'], content['movement_type'],
                content['phone_num'], content['have_partner'])
            regular_trainer.id = trainer_id
            trainer_manager.update(regular_trainer)
            response = app.response_class(status=200)
        elif content['type'] == 'Gym Leader':
            gym_leader = GymLeader(content['name'], content['pokemon_team'],
                                   content['trainer_class'],
                                   content['pokecoins'], content['location'],
                                   content['badge'], content['element'],
                                   content['prize'])
            gym_leader.id = trainer_id
            trainer_manager.update(gym_leader)
            response = app.response_class(status=200)
        else:
            response = app.response_class(
                response='Type not supported', status=404)
    except Exception as e:
        response = app.response_class(response=str(e), status=404)
    return response


@app.route('/trainermanager/trainers/<int:trainer_id>', methods=['DELETE'])
def delete_trainer(trainer_id):
    '''Delete entity JSON in Trainer Manager'''
    try:
        trainer_manager.delete(trainer_id)
        response = app.response_class(status=200)
    except Exception as e:
        response = app.response_class(response=str(e), status=404)
    return response


@app.route('/trainermanager/trainers/<int:trainer_id>', methods=['GET'])
def get_trainer_by_id(trainer_id):
    '''Get entity JSON by ID in Trainer Manager'''
    try:
        result = trainer_manager.get_trainer_by_id(trainer_id)
        if result is not None:
            response = app.response_class(
                status=200,
                response=json.dumps(result.to_dict()),
                mimetype='application/json')
        else:
            response = app.response_class(
                response='ID not found in database', status=404)
    except Exception as e:
        response = app.response_class(response=str(e), status=404)
    return response


@app.route('/trainermanager/trainers/all', methods=['GET'])
def get_all_trainers():
    '''Gets all trainers'''
    trainer_dict_list = []
    for curr_trainer in trainer_manager.get_all():
        trainer_dict_list.append(curr_trainer.to_dict())
    return app.response_class(
        status=200,
        response=json.dumps(trainer_dict_list),
        mimetype='application/json')


@app.route('/trainermanager/trainers/all/<type>', methods=['GET'])
def get_all_trainers_by_type(type):
    '''Gets all trainers by type'''
    if type == 'regular_trainer':
        type = 'Regular Trainer'
    elif type == 'gym_leader':
        type = 'Gym Leader'
    else:
        return app.response_class(response='Type not supported', status=400)

    trainer_dict_list = []
    for curr_trainer in trainer_manager.get_all_by_type(type):
        trainer_dict_list.append(curr_trainer.to_dict())
    try:
        response = app.response_class(
            status=200,
            response=json.dumps(trainer_dict_list),
            mimetype='application/json')
    except Exception as e:
        response = app.response_class(response=str(e), status=400)
    return response


@app.route('/trainermanager/trainers/stats', methods=['GET'])
def get_stats():
    '''Get stats for trainer manager'''
    stat = trainer_manager.get_stats()
    result = [
        'Number of Trainers: %d' % stat.get_num_trainers(),
        'Number of Gym Leaders: %d' % stat.get_num_gym_leader(),
        'Number of Regular Trainers: %d' % stat.get_num_regular_trainer(),
        'Number of Trainers With Partners: %d' %
        stat.get_num_trainer_have_partner(),
        ('Trainers per location: {}').format(stat.get_num_per_location())
    ]
    return app.response_class(
        status=200, response=json.dumps(result), mimetype='application/json')


if __name__ == "__main__":
    app.run()
