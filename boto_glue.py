import boto3
import json

ACCESS_KEY_ID = ''
SECRET_ACCESS_KEY = ''


client = boto3.client('glue', region_name="us-east-1", aws_access_key_id=ACCESS_KEY_ID,
    aws_secret_access_key=SECRET_ACCESS_KEY)



response = client.create_crawler(
    Name='S3Crawler',
    Role='GlueFullAccess',
    DatabaseName='S3CrawlerHOC',
    Targets={
        'S3Targets': [
            {
                'Path': 's3://glue-source-hoc/read',
                'Exclusions': [
                    'string',
                ],
                'SampleSize': 2
            },
            {
                'Path': 's3://glue-source-hoc/write',
                'Exclusions': [
                    'string',
                ],
                'SampleSize': 2
            },
        ]
    },
    Schedule='cron(15 12 * * ? *)',
    SchemaChangePolicy={
        'UpdateBehavior': 'UPDATE_IN_DATABASE',
        'DeleteBehavior': 'DEPRECATE_IN_DATABASE'
    },
    RecrawlPolicy={
        'RecrawlBehavior': 'CRAWL_EVERYTHING'
    },
    LineageConfiguration={
        'CrawlerLineageSettings': 'DISABLE'
    }
)

print(json.dumps(response, indent=4, sort_keys=True, default=str))