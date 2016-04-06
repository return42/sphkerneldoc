
.. _media-ioc-enum-entities:

=============================
ioctl MEDIA_IOC_ENUM_ENTITIES
=============================

*man MEDIA_IOC_ENUM_ENTITIES(2)*

Enumerate entities and their properties


Synopsis
========

.. c:function:: int ioctl( int fd, int request, struct media_entity_desc *argp )

Arguments
=========

``fd``
    File descriptor returned by :ref:`open() <media-func-open>`.

``request``
    MEDIA_IOC_ENUM_ENTITIES

``argp``


Description
===========

To query the attributes of an entity, applications set the id field of a struct :ref:`media_entity_desc <media-entity-desc>` structure and call the MEDIA_IOC_ENUM_ENTITIES
ioctl with a pointer to this structure. The driver fills the rest of the structure or returns an EINVAL error code when the id is invalid.

Entities can be enumerated by or'ing the id with the ``MEDIA_ENT_ID_FLAG_NEXT`` flag. The driver will return information about the entity with the smallest id strictly larger than
the requested one ('next entity'), or the EINVAL error code if there is none.

Entity IDs can be non-contiguous. Applications must *not* try to enumerate entities by calling MEDIA_IOC_ENUM_ENTITIES with increasing id's until they get an error.


.. _media-entity-desc:

struct media_entity_desc
========================

::

    TODO ... 


    <table pgwide="1" frame="none" id="media-entity-desc">
          <title>struct <structname>media_entity_desc</structname></title>
          <tgroup cols="5">
        <colspec colname="c1"/>
        <colspec colname="c2"/>
        <colspec colname="c3"/>
        <colspec colname="c4"/>
        <colspec colname="c5"/>
        <tbody valign="top">
          <row>
            <entry>__u32</entry>
            <entry><structfield>id</structfield></entry>
            <entry/>
            <entry/>
            <entry>Entity id, set by the application. When the id is or'ed with
            <constant>MEDIA_ENT_ID_FLAG_NEXT</constant>, the driver clears the
            flag and returns the first entity with a larger id.</entry>
          </row>
          <row>
            <entry>char</entry>
            <entry><structfield>name</structfield>[32]</entry>
            <entry/>
            <entry/>
            <entry>Entity name as an UTF-8 NULL-terminated string.</entry>
          </row>
          <row>
            <entry>__u32</entry>
            <entry><structfield>type</structfield></entry>
            <entry/>
            <entry/>
            <entry>Entity type, see <xref linkend="media-entity-type"/> for details.</entry>
          </row>
          <row>
            <entry>__u32</entry>
            <entry><structfield>revision</structfield></entry>
            <entry/>
            <entry/>
            <entry>Entity revision. Always zero (obsolete)</entry>
          </row>
          <row>
            <entry>__u32</entry>
            <entry><structfield>flags</structfield></entry>
            <entry/>
            <entry/>
            <entry>Entity flags, see <xref linkend="media-entity-flag"/> for details.</entry>
          </row>
          <row>
            <entry>__u32</entry>
            <entry><structfield>group_id</structfield></entry>
            <entry/>
            <entry/>
            <entry>Entity group ID. Always zero (obsolete)</entry>
          </row>
          <row>
            <entry>__u16</entry>
            <entry><structfield>pads</structfield></entry>
            <entry/>
            <entry/>
            <entry>Number of pads</entry>
          </row>
          <row>
            <entry>__u16</entry>
            <entry><structfield>links</structfield></entry>
            <entry/>
            <entry/>
            <entry>Total number of outbound links. Inbound links are not counted
            in this field.</entry>
          </row>
          <row>
            <entry>union</entry>
          </row>
          <row>
            <entry/>
            <entry>struct</entry>
            <entry><structfield>dev</structfield></entry>
            <entry/>
            <entry>Valid for (sub-)devices that create a single device node.</entry>
          </row>
          <row>
            <entry/>
            <entry/>
            <entry>__u32</entry>
            <entry><structfield>major</structfield></entry>
            <entry>Device node major number.</entry>
          </row>
          <row>
            <entry/>
            <entry/>
            <entry>__u32</entry>
            <entry><structfield>minor</structfield></entry>
            <entry>Device node minor number.</entry>
          </row>
          <row>
            <entry/>
            <entry>__u8</entry>
            <entry><structfield>raw</structfield>[184]</entry>
            <entry/>
            <entry/>
          </row>
        </tbody>
          </tgroup>
        </table>



Return Value
============

On success 0 is returned, on error -1 and the ``errno`` variable is set appropriately. The generic error codes are described at the :ref:`Generic Error Codes <gen-errors>`
chapter.

EINVAL
    The struct :ref:`media_entity_desc <media-entity-desc>` ``id`` references a non-existing entity.
