
.. _useful-functions:

================
Useful Functions
================


.. _useful-functions-snd-printk:

snd_printk() and friends
========================

ALSA provides a verbose version of the ``printk()`` function. If a kernel config ``CONFIG_SND_VERBOSE_PRINTK`` is set, this function prints the given message together with the file
name and the line of the caller. The ``KERN_XXX`` prefix is processed as well as the original ``printk()`` does, so it's recommended to add this prefix, e.g.


.. code-block:: c

      snd_printk(KERN_ERR "Oh my, sorry, it's extremely bad!n");

There are also ``printk()``'s for debugging. ``snd_printd()`` can be used for general debugging purposes. If ``CONFIG_SND_DEBUG`` is set, this function is compiled, and works just
like ``snd_printk()``. If the ALSA is compiled without the debugging flag, it's ignored.

``snd_printdd()`` is compiled in only when ``CONFIG_SND_DEBUG_VERBOSE`` is set. Please note that ``CONFIG_SND_DEBUG_VERBOSE`` is not set as default even if you configure the
alsa-driver with ``--with-debug=full`` option. You need to give explicitly ``--with-debug=detect`` option instead.


.. _useful-functions-snd-bug:

snd_BUG()
=========

It shows the



::

    BUG?
message and stack trace as well as ``snd_BUG_ON`` at the point. It's useful to show that a fatal error happens there.

When no debug flag is set, this macro is ignored.


.. _useful-functions-snd-bug-on:

snd_BUG_ON()
============

``snd_BUG_ON()`` macro is similar with ``WARN_ON()`` macro. For example,


.. code-block:: c

      snd_BUG_ON(!pointer);

or it can be used as the condition,


.. code-block:: c

      if (snd_BUG_ON(non_zero_is_bug))
              return -EINVAL;

The macro takes an conditional expression to evaluate. When ``CONFIG_SND_DEBUG``, is set, if the expression is non-zero, it shows the warning message such as



::

    BUG? (xxx)
normally followed by stack trace. In both cases it returns the evaluated value.
