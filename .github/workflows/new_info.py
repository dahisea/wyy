#更新refresh_toke
name: update_refresh

on: 
  release:
    types: [published]
  push:
    tags:
    - 'v*'
  #  branches: 
  #    - master
  schedule:
    - cron: "0 16 * * *"
  watch:
    types: [started]
   
jobs:
  build:
    runs-on: ubuntu-latest
    
    steps:
    - name: Checkout
      uses: actions/checkout@master
    - name: Set up Python #安装python
      uses: actions/setup-python@v1
      with:
        python-version: 3.8
    - name: Install requests #安装requests
      run: |
        pip install requests
    - name: Delete secrets config #删除机密
      run: | 
        rm -f io.md
        touch io.md
    - name: Push changes
      uses: ad-m/github-push-action@master
      with:
        github_token: ${{ secrets.GITHUB_TOKEN }}
