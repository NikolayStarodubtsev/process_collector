========
Overview
========

process_collector is a simple application which collects info about
processes and services running in current environment. Collected data is
packed in JSON for future analysis.
The following information about process is collected:

* The name of the user who started the process.

* The time when process was started.

* Path to executable file.

* Command line arguments.

* Network ports which was opened by process.

* Children of this process.

* Information about executable file.
