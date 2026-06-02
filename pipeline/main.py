import multiprocessing

def run_skincare():
    import pipeline.skincare

def run_makeup():
    import pipeline.makeup

def run_entry():
    import pipeline.entry

def run_storeroom():
    import pipeline.storeroom

def run_billing():
    import pipeline.billing

if __name__ == "__main__":

    processes = [

        multiprocessing.Process(target=run_skincare),

        multiprocessing.Process(target=run_makeup),

        multiprocessing.Process(target=run_entry),

        multiprocessing.Process(target=run_storeroom),

        multiprocessing.Process(target=run_billing)

    ]

    for p in processes:
        p.start()

    for p in processes:
        p.join()
