export HTTPS_PROXY=http://192.168.71.25:8080
export HF_HUB_ENABLE_HF_TRANSFER=1
export HF_ENDPOINT="https://hf-mirror.com"
export HF_TOKEN="hf_..." # Get your token from https://huggingface.co/settings/tokens

# repo_id="lerobot/aloha_mobile_cabinet"
repo_id="lerobot/diffusion_pusht"
repo_type="model" # "model", "dataset", "space"
cache_dir="../data/${repo_type}/.cache"
save_dir="../data/${repo_type}"


huggingface-cli download --resume-download --repo-type=${repo_type} --cache-dir=${cache_dir} --local-dir="${save_dir}/${repo_id}" ${repo_id}
