```yaml
jobs:
  tag-alert:
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v2
        with:
          fetch-depth: 0

      - name: Publish Tag Notification
        uses: inmar/actions-sns-tag-alert@master
        with:
          aws_key_id: ${{ secrets.AWS_ACCESS_KEY_ID }}
          aws_secret_key: ${{ secrets.AWS_SECRET_ACCESS_KEY }}
          topic_arn: "arn:aws:sns:us-east-1:0123456789012:event_topic"
```
