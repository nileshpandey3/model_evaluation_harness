"""
Multi-turn travel-planning scenarios for conversation evaluation
"""

def get_travel_planning_scenario():
    return {
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
        ],
        "expectations": {"final_trip_days": 1},
    }

def get_all_scenarios() -> list[dict | None]:
    return [
        get_travel_planning_scenario(),
    ]
