DELIMITER = '\t'
# print(DELIMITER.join[col1_name, col2_name, col3_name, col4_name])

us_capitals_by_state = {
    'Alabama': 'Montgomery',
    'Alaska': 'Juneau'
}

# Capital names only
capitals = us_capitals_by_state.values()
print(capitals)
print(sorted(capitals))

def get_united_states_capitals(caps_by_state):
    capitals = caps_by_state.values()
    return sorted(capitals)

print(get_united_states_capitals(us_capitals_by_state))