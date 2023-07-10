import multiprocessing
from job_scheduler.job import Job
from job_scheduler.jobs.test_job import TestJob


class JobScheduler:
    """
    This class is responsible for managing and running jobs.
    It has a method to run a job.
    Add your jobs in the init method.
    """
    def __init__(self):
        self.jobs = {
            "TestJob": TestJob
        }

    def run_job(self, job_name, **kwargs):
        """
        This method takes in a job name and parameters, and runs the job in a separate process.
        """
        if job_name not in self.jobs:
            raise ValueError("Job not found")
        job = self.jobs[job_name]
        process = multiprocessing.Process(target=job.process, args=[job], kwargs=kwargs)
        process.start()
        return True
