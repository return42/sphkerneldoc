.. -*- coding: utf-8; mode: rst -*-

.. _proc-interface:

==============
Proc Interface
==============

ALSA provides an easy interface for procfs. The proc files are very
useful for debugging. I recommend you set up proc files if you write a
driver and want to get a running status or register dumps. The API is
found in ``<sound/info.h>``.

To create a proc file, call ``snd_card_proc_new()``.


.. code-block:: c

      struct snd_info_entry *entry;
      int err = snd_card_proc_new(card, "my-file", &entry);

where the second argument specifies the name of the proc file to be
created. The above example will create a file ``my-file`` under the card
directory, e.g. ``/proc/asound/card0/my-file``.

Like other components, the proc entry created via
``snd_card_proc_new()`` will be registered and released automatically in
the card registration and release functions.

When the creation is successful, the function stores a new instance in
the pointer given in the third argument. It is initialized as a text
proc file for read only. To use this proc file as a read-only text file
as it is, set the read callback with a private data via
``snd_info_set_text_ops()``.


.. code-block:: c

      snd_info_set_text_ops(entry, chip, my_proc_read);

where the second argument (``chip``) is the private data to be used in
the callbacks. The third parameter specifies the read buffer size and
the fourth (``my_proc_read``) is the callback function, which is defined
like


.. code-block:: c

      static void my_proc_read(struct snd_info_entry *entry,
                               struct snd_info_buffer *buffer);

In the read callback, use ``snd_iprintf()`` for output strings, which
works just like normal ``printf()``. For example,


.. code-block:: c

      static void my_proc_read(struct snd_info_entry *entry,
                               struct snd_info_buffer *buffer)
      {
              struct my_chip *chip = entry->private_data;

              snd_iprintf(buffer, "This is my chip!n");
              snd_iprintf(buffer, "Port = %ldn", chip->port);
      }

The file permissions can be changed afterwards. As default, it's set as
read only for all users. If you want to add write permission for the
user (root as default), do as follows:


.. code-block:: c

     entry->mode = S_IFREG | S_IRUGO | S_IWUSR;

and set the write buffer size and the callback


.. code-block:: c

      entry->c.text.write = my_proc_write;

For the write callback, you can use ``snd_info_get_line()`` to get a
text line, and ``snd_info_get_str()`` to retrieve a string from the
line. Some examples are found in ``core/oss/mixer_oss.c``, core/oss/and
``pcm_oss.c``.

For a raw-data proc-file, set the attributes as follows:


.. code-block:: c

      static struct snd_info_entry_ops my_file_io_ops = {
              .read = my_file_io_read,
      };

      entry->content = SNDRV_INFO_CONTENT_DATA;
      entry->private_data = chip;
      entry->c.ops = &my_file_io_ops;
      entry->size = 4096;
      entry->mode = S_IFREG | S_IRUGO;

For the raw data, ``size`` field must be set properly. This specifies
the maximum size of the proc file access.

The read/write callbacks of raw mode are more direct than the text mode.
You need to use a low-level I/O functions such as
``copy_from/to_user()`` to transfer the data.


.. code-block:: c

      static ssize_t my_file_io_read(struct snd_info_entry *entry,
                                  void *file_private_data,
                                  struct file *file,
                                  char *buf,
                                  size_t count,
                                  loff_t pos)
      {
              if (copy_to_user(buf, local_data + pos, count))
                      return -EFAULT;
              return count;
      }

If the size of the info entry has been set up properly, ``count`` and
``pos`` are guaranteed to fit within 0 and the given size. You don't
have to check the range in the callbacks unless any other condition is
required.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
