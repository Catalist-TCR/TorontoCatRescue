ssh $DEPLOY_SERVER_USER@$DEPLOY_SERVER_ADDRESS mkdir -p $DEPLOY_SERVER_PATH
rsync -r --delete-after --exclude="deploy_key*" --exclude="*.md" --exclude="scripts/" --quiet $TRAVIS_BUILD_DIR/ $DEPLOY_SERVER_USER@$DEPLOY_SERVER_ADDRESS:$DEPLOY_SERVER_PATH

