from module5_mod import NumberProcessor

if __name__ == "__main__":
    processor = NumberProcessor()
    while True:
        should_continue = processor.run()
        if not should_continue:
            break
        
        choice = input("Would you like to perform another search? (y/n): ").lower()
        if choice != 'y':
            print("Exiting program...")
            break
        
        # Reset for new search
        processor.__init__()