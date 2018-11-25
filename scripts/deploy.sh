#!/bin/bash
rsync -r --delete-after --exclude="deploy_key*" --exclude=".git*" --exclude="*.md" --exclude="env/" --exclude="scripts/" --quiet $TRAVIS_BUILD_DIR/ $DEPLOY_SERVER_USER@$DEPLOY_SERVER_ADDRESS:$DEPLOY_SERVER_PATH
ssh $DEPLOY_SERVER_USER@$DEPLOY_SERVER_ADDRESS python3 -m venv $DEPLOY_SERVER_PATH/env
ssh $DEPLOY_SERVER_USER@$DEPLOY_SERVER_ADDRESS $DEPLOY_SERVER_PATH/env/bin/pip install -r $DEPLOY_SERVER_PATH/requirements.txt
ssh $DEPLOY_SERVER_USER@$DEPLOY_SERVER_ADDRESS sudo systemctl restart catalist
