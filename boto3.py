import boto3

def create_codeguru_review(repository_name):
    client = boto3.client('codeguru-reviewer')

    response = client.create_code_review(
        Name='MyCodeReview',
        RepositoryAssociation={
            'RepositoryName': repository_name,
            'Owner': 'your-github-username',
            'ProviderType': 'GitHub',
            'ConnectionArn': 'arn:aws:codestar-connections:us-west-2:123456789012:connection/connection-id'
        },
        Type='PullRequest',
        PullRequestId='1234567890',
        CommitId='abcdefg123456',
        Metrics={
            'FindingsCount': 10,
            'MeteredLinesOfCodeCount': 1000
        },
        ClientRequestToken='a-unique-token',
        Tags={
            'my-tag-key': 'my-tag-value'
        }
    )

    return response['CodeReviewArn']

def describe_codeguru_review(code_review_arn):
    client = boto3.client('codeguru-reviewer')

    response = client.describe_code_review(
        CodeReviewArn=code_review_arn
    )

    return response

# Example usage
repository_name = 'my-repo'
code_review_arn = create_codeguru_review(repository_name)
review_details = describe_codeguru_review(code_review_arn)

print('Code Review Details:')
print('-------------------')
print('Name:', review_details['Name'])
print('Status:', review_details['State']['Name'])
print('Repository:', review_details['RepositoryAssociation']['RepositoryName'])
print('Owner:', review_details['RepositoryAssociation']['Owner'])
