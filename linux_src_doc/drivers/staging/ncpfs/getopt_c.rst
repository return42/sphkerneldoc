.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/staging/ncpfs/getopt.c

.. _`ncp_getopt`:

ncp_getopt
==========

.. c:function:: int ncp_getopt(const char *caller, char **options, const struct ncp_option *opts, char **optopt, char **optarg, unsigned long *value)

    option parser

    :param const char \*caller:
        name of the caller, for error messages

    :param char \*\*options:
        the options string

    :param const struct ncp_option \*opts:
        an array of \ :c:type:`struct option <option>`\  entries controlling parser operations

    :param char \*\*optopt:
        output; will contain the current option

    :param char \*\*optarg:
        output; will contain the value (if one exists)

    :param unsigned long \*value:
        output; may be NULL; will be overwritten with the integer value
        of the current argument.

.. _`ncp_getopt.description`:

Description
-----------

Helper to parse options on the format used by mount ("a=b,c=d,e,f").
Returns opts->val if a matching entry in the 'opts' array is found,
0 when no more tokens are found, -1 if an error is encountered.

.. This file was automatic generated / don't edit.

