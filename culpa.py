import logging
import time

def process_python_script(script_path):
    """
    Process the Python script located at 'script_path'.
    This includes error handling and performance logging.
    """
    start_time = time.time()
    
    try:
        # Assuming 'script_path' is a path to a Python file that needs to be executed
        with open(script_path, 'r') as script_file:
            exec(script_file.read())
            
        # Log the success of the script execution
        logging.info(f"Successfully processed the script: {script_path}")
        
    except Exception as e:
        # Log any errors that occur during the script execution
        logging.error(f"An error occurred while processing the script: {script_path}")
        logging.error(str(e))
        
    finally:
        # Calculate and log the time taken to process the script
        end_time = time.time()
        processing_time = end_time - start_time
        logging.info(f"Time taken to process the script: {processing_time:.2f} seconds")

# Example usage:
# process_python_script('path/to/your_script.py')
