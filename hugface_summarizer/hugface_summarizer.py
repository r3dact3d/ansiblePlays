# hugface_summarizer.py

from ansible.module_utils.basic import AnsibleModule
from huggingface_hub import InferenceClient

DOCUMENTATION = '''
---
module: hugface_summarizer
short_description: Perform text summarization using Hugging Face models
description:
    - This module uses the Hugging Face Inference Client to perform text summarization.
    - It takes in a text input and returns a summarized version of the text.
options:
    text:
        description:
            - The text to be summarized.
        required: true
        type: str
    model:
        description:
            - The Hugging Face model to use for summarization.
        required: false
        type: str
        default: "t5-small"
author:
    - Brady Thompson (@bradyt@redhat.com)
'''

EXAMPLES = '''
- name: Summarize text
  hugface_summarizer:
    text: "This is a long piece of text that needs to be summarized."
  register: summary

- name: Print the summary
  debug:
    var: summary
'''

RETURN = '''
summary:
    description: The summarized text.
    returned: always
    type: str
'''

def main():
    module = AnsibleModule(
        argument_spec=dict(
            text=dict(required=True, type='str'),
            model=dict(required=False, type='str', default='t5-small')
        ),
        supports_check_mode=True
    )

    text = module.params['text']
    model = module.params['model']

    try:
        client = InferenceClient()
        summary = client.summarization(text, model=model)
        module.exit_json(changed=False, summary=summary)
    except Exception as e:
        module.fail_json(msg=str(e))

if __name__ == '__main__':
    main()