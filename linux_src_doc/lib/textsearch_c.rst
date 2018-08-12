.. -*- coding: utf-8; mode: rst -*-
.. src-file: lib/textsearch.c

.. _`ts_intro`:

ts_intro
========

INTRODUCTION

  The textsearch infrastructure provides text searching facilities for
  both linear and non-linear data. Individual search algorithms are
  implemented in modules and chosen by the user.

ARCHITECTURE

.. code-block:: none

    User
    +----------------+
    |        finish()|<--------------(6)-----------------+
    |get_next_block()|<--------------(5)---------------+ |
    |                |                     Algorithm   | |
    |                |                    +------------------------------+
    |                |                    |  init()   find()   destroy() |
    |                |                    +------------------------------+
    |                |       Core API           ^       ^          ^
    |                |      +---------------+  (2)     (4)        (8)
    |             (1)|----->| prepare()     |---+       |          |
    |             (3)|----->| find()/next() |-----------+          |
    |             (7)|----->| destroy()     |----------------------+
    +----------------+      +---------------+

  (1) User configures a search by calling textsearch_prepare() specifying
      the search parameters such as the pattern and algorithm name.
  (2) Core requests the algorithm to allocate and initialize a search
      configuration according to the specified parameters.
  (3) User starts the search(es) by calling textsearch_find() or
      textsearch_next() to fetch subsequent occurrences. A state variable
      is provided to the algorithm to store persistent variables.
  (4) Core eventually resets the search offset and forwards the find()
      request to the algorithm.
  (5) Algorithm calls get_next_block() provided by the user continuously
      to fetch the data to be searched in block by block.
  (6) Algorithm invokes finish() after the last call to get_next_block
      to clean up any leftovers from get_next_block. (Optional)
  (7) User destroys the configuration by calling textsearch_destroy().
  (8) Core notifies the algorithm to destroy algorithm specific
      allocations. (Optional)

USAGE

  Before a search can be performed, a configuration must be created
  by calling \ :c:func:`textsearch_prepare`\  specifying the searching algorithm,
  the pattern to look for and flags. As a flag, you can set TS_IGNORECASE
  to perform case insensitive matching. But it might slow down
  performance of algorithm, so you should use it at own your risk.
  The returned configuration may then be used for an arbitrary
  amount of times and even in parallel as long as a separate struct
  ts_state variable is provided to every instance.

  The actual search is performed by either calling
  \ :c:func:`textsearch_find_continuous`\  for linear data or by providing
  an own \ :c:func:`get_next_block`\  implementation and
  calling \ :c:func:`textsearch_find`\ . Both functions return
  the position of the first occurrence of the pattern or UINT_MAX if
  no match was found. Subsequent occurrences can be found by calling
  \ :c:func:`textsearch_next`\  regardless of the linearity of the data.

  Once you're done using a configuration it must be given back via
  textsearch_destroy.

EXAMPLE::

  int pos;
  struct ts_config *conf;
  struct ts_state state;
  const char *pattern = "chicken";
  const char *example = "We dance the funky chicken";

  conf = textsearch_prepare("kmp", pattern, strlen(pattern),
                            GFP_KERNEL, TS_AUTOLOAD);
  if (IS_ERR(conf)) {
      err = PTR_ERR(conf);
      goto errout;
  }

  pos = textsearch_find_continuous(conf, \&state, example, strlen(example));
  if (pos != UINT_MAX)
      panic("Oh my god, dancing chickens at \%d\n", pos);

  textsearch_destroy(conf);

.. _`textsearch_register`:

textsearch_register
===================

.. c:function:: int textsearch_register(struct ts_ops *ops)

    register a textsearch module

    :param struct ts_ops \*ops:
        operations lookup table

.. _`textsearch_register.description`:

Description
-----------

This function must be called by textsearch modules to announce
their presence. The specified &@ops must have \ ``name``\  set to a
unique identifier and the callbacks \ :c:func:`find`\ , \ :c:func:`init`\ , \ :c:func:`get_pattern`\ ,
and \ :c:func:`get_pattern_len`\  must be implemented.

Returns 0 or -EEXISTS if another module has already registered
with same name.

.. _`textsearch_unregister`:

textsearch_unregister
=====================

.. c:function:: int textsearch_unregister(struct ts_ops *ops)

    unregister a textsearch module

    :param struct ts_ops \*ops:
        operations lookup table

.. _`textsearch_unregister.description`:

Description
-----------

This function must be called by textsearch modules to announce
their disappearance for examples when the module gets unloaded.
The \ :c:type:`struct ops <ops>`\  parameter must be the same as the one during the
registration.

Returns 0 on success or -ENOENT if no matching textsearch
registration was found.

.. _`textsearch_find_continuous`:

textsearch_find_continuous
==========================

.. c:function:: unsigned int textsearch_find_continuous(struct ts_config *conf, struct ts_state *state, const void *data, unsigned int len)

    search a pattern in continuous/linear data

    :param struct ts_config \*conf:
        search configuration

    :param struct ts_state \*state:
        search state

    :param const void \*data:
        data to search in

    :param unsigned int len:
        length of data

.. _`textsearch_find_continuous.description`:

Description
-----------

A simplified version of \ :c:func:`textsearch_find`\  for continuous/linear data.
Call \ :c:func:`textsearch_next`\  to retrieve subsequent matches.

Returns the position of first occurrence of the pattern or
\ ``UINT_MAX``\  if no occurrence was found.

.. _`textsearch_prepare`:

textsearch_prepare
==================

.. c:function:: struct ts_config *textsearch_prepare(const char *algo, const void *pattern, unsigned int len, gfp_t gfp_mask, int flags)

    Prepare a search

    :param const char \*algo:
        name of search algorithm

    :param const void \*pattern:
        pattern data

    :param unsigned int len:
        length of pattern

    :param gfp_t gfp_mask:
        allocation mask

    :param int flags:
        search flags

.. _`textsearch_prepare.description`:

Description
-----------

Looks up the search algorithm module and creates a new textsearch
configuration for the specified pattern.

.. _`textsearch_prepare.note`:

Note
----

The format of the pattern may not be compatible between
      the various search algorithms.

Returns a new textsearch configuration according to the specified
parameters or a \ :c:func:`ERR_PTR`\ . If a zero length pattern is passed, this
function returns EINVAL.

.. _`textsearch_destroy`:

textsearch_destroy
==================

.. c:function:: void textsearch_destroy(struct ts_config *conf)

    destroy a search configuration

    :param struct ts_config \*conf:
        search configuration

.. _`textsearch_destroy.description`:

Description
-----------

Releases all references of the configuration and frees
up the memory.

.. This file was automatic generated / don't edit.

