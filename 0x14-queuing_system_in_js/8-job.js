export default function createPushNotificationsJobs(jobs, queue) {
    if (Object.getPrototypeOf(jobs) !== Array.prototype) throw Error('Jobs is not an array');

    jobs.forEach((job) => {
        const singleJob = queue.create('push_notification_code_3', job).save(
            (err) => {
                if (!err) console.log(`Notification job created: ${singleJob.id}`);
            });

        singleJob.on('complete', () => console.log(`Notification job ${singleJob.id} completed`));
        singleJob.on('failed', (err) => console.log(`Notification job ${singleJob.id} failed: ${err}`));
        singleJob.on('progress', (progress) => console.log(`Notification job ${singleJob.id} ${progress}% complete`));
    });
}
