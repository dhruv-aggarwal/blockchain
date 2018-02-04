import json
from app.managers.sync import sync, sync_local
from app import app

sync(True)


@app.route('/blockchain.json', methods=['GET'])
def blockchain():
    '''
    Shoots back the blockchain, which in our case, is a json list of hashes
    with the block information which is:
    index
    timestamp
    data
    hash
    prev_hash
    '''
    node_blocks = sync_local()  # regrab the nodes if they've changed
    # Convert our blocks into dictionaries
    # so we can send them as json objects later
    python_blocks = []
    for block in node_blocks:
        python_blocks.append(block.__dict__())
    json_blocks = json.dumps(python_blocks)
    return json_blocks
