from job_scheduler.scheduler import JobScheduler
scheduler = JobScheduler()


def run_job(job_name, kwargs):
    try:
        return scheduler.run_job(job_name, **kwargs)
    except:
        # ADD ALERT HERE
        return False


if __name__ == "__main__":
    run_job("TestJob", {"name": "Chanandler Bong"})
