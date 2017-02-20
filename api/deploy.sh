cd openfisca-cnous
git checkout dev_cnous -f
pip install -r api/requirements.txt --upgrade --user
pip install -e . --user
forever stop openfisca || echo "No openfisca was running"
forever --uid openfisca -l openfisca.log -e openfisca_error.log --append start -c "paster serve" api/api_config.ini
