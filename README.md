# The World's Simplest Job Scheduler (Probably)

Welcome to the world's simplest job scheduler! This is a lightweight, no-frills job scheduler designed to take care of your asynchronous task execution needs with simplicity and ease.

## Features

- **Asynchronous Execution:** Capable of running multiple jobs concurrently, freeing up your main application thread.
- **Simplicity:** No complex configurations or steep learning curves. Just straightforward job scheduling.
- **Efficient:** Designed to get your jobs up and running quickly.

## Perfect Companion for APIs

This job scheduler pairs perfectly with APIs, especially those that require an immediate response. For example, you might have a webhook that receives input from Stripe and needs to perform a task based on that input. Instead of making Stripe wait for your task to finish, you can simply schedule the task to run asynchronously and immediately return a success response. This keeps your API responsive and prevents timeouts.

## How to Add a Job

1. **Create a new job class:** Create a new Python class for your job in the `jobs` directory. Your class should inherit from the `Job` class.

    ```python
    from job_scheduler.job import Job
    
    class MyAwesomeJob(Job):
        def process(self, **kwargs):
            # Implement your job logic here
            pass
    ```
    
2. **Add your job to the JobScheduler:** Add your job to the `jobs` dictionary in the `JobScheduler` class. Use the name of your job as the key and your job class as the value.

    ```python
    class JobScheduler:
        def __init__(self):
            self.jobs = {
                "TestJob": TestJob,
                "MyAwesomeJob": MyAwesomeJob
            }
    ```
    
That's it! You've just added a job to the world's simplest job scheduler. Your job is now ready to run asynchronously in its own process.

**Disclaimer:** This job scheduler does not provide features found in larger job schedulers such as job persistence, retries, or distributed execution. It's designed for simplicity and ease of use.
