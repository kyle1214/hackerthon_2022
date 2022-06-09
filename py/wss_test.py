from substrateinterface import SubstrateInterface


substrate = SubstrateInterface(
    url="ws://127.0.0.1:9944"
)   

def get_collator_list():
    
    result = substrate.query(
        module='ParachainStaking',
        storage_function='CandidatePool'
    )
    print(result)

def main():
    get_collator_list()
if __name__ == "__main__":
    main()