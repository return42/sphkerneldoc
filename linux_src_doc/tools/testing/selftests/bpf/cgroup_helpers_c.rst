.. -*- coding: utf-8; mode: rst -*-
.. src-file: tools/testing/selftests/bpf/cgroup_helpers.c

.. _`setup_cgroup_environment`:

setup_cgroup_environment
========================

.. c:function:: int setup_cgroup_environment( void)

    Setup the cgroup environment

    :param  void:
        no arguments

.. _`setup_cgroup_environment.description`:

Description
-----------

After calling this function, cleanup_cgroup_environment should be called
once testing is complete.

This function will print an error to stderr and return 1 if it is unable
to setup the cgroup environment. If setup is successful, 0 is returned.

.. _`join_cgroup`:

join_cgroup
===========

.. c:function:: int join_cgroup(char *path)

    Join a cgroup

    :param char \*path:
        The cgroup path, relative to the workdir, to join

.. _`join_cgroup.description`:

Description
-----------

This function expects a cgroup to already be created, relative to the cgroup
work dir, and it joins it. For example, passing "/my-cgroup" as the path
would actually put the calling process into the cgroup
"/cgroup-test-work-dir/my-cgroup"

On success, it returns 0, otherwise on failure it returns 1.

.. _`cleanup_cgroup_environment`:

cleanup_cgroup_environment
==========================

.. c:function:: void cleanup_cgroup_environment( void)

    Cleanup Cgroup Testing Environment

    :param  void:
        no arguments

.. _`cleanup_cgroup_environment.description`:

Description
-----------

This is an idempotent function to delete all temporary cgroups that
have been created during the test, including the cgroup testing work
directory.

At call time, it moves the calling process to the root cgroup, and then
runs the deletion process. It is idempotent, and should not fail, unless
a process is lingering.

On failure, it will print an error to stderr, and try to continue.

.. _`create_and_get_cgroup`:

create_and_get_cgroup
=====================

.. c:function:: int create_and_get_cgroup(char *path)

    Create a cgroup, relative to workdir, and get the FD

    :param char \*path:
        The cgroup path, relative to the workdir, to join

.. _`create_and_get_cgroup.description`:

Description
-----------

This function creates a cgroup under the top level workdir and returns the
file descriptor. It is idempotent.

On success, it returns the file descriptor. On failure it returns 0.
If there is a failure, it prints the error to stderr.

.. _`get_cgroup_id`:

get_cgroup_id
=============

.. c:function:: unsigned long long get_cgroup_id(char *path)

    Get cgroup id for a particular cgroup path

    :param char \*path:
        The cgroup path, relative to the workdir, to join

.. _`get_cgroup_id.description`:

Description
-----------

On success, it returns the cgroup id. On failure it returns 0,
which is an invalid cgroup id.
If there is a failure, it prints the error to stderr.

.. This file was automatic generated / don't edit.

