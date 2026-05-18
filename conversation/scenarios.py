

def travel_planning_scenario():
    """

    """
    scenario = {
        'name': 'Travel Planning Conversation',
        'constraint': {
            'type': 'max_budget',
            'currency': 'USD',
            'value': 500
        },
        'turns': [
            {
                'role': 'user',
                'content': 'Plan me a 3 day trip to Las Vegas from Los Angeles for 2 people'
            },
            {
                'role': 'user',
                'content': "Lets's make it a one day trip keeping the same budget"

            }
        ]
    }

    return scenario