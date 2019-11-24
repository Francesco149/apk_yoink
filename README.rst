simple command line tool that lets you download android apps by package
name, including region locked ones

it also checks whether your previously downloaded apks are up to date

you need python3, ideally 3.7+

this depends on gachanator which i haven't put on pip yet, so install that
first:

.. code-block:: sh

    cd
    git clone https://github.com/Francesco149/gachanator
    cd gachanator
    python3 -m pip install .

then you can install and use apk-yoink:

.. code-block:: sh

    cd
    git clone https://github.com/Francesco149/apk_yoink
    cd apk_yoink
    python3 -m pip install .
    apk-yoink com.klab.lovelive.allstars

remember that you need to add the pip scripts folder to your PATH, which
usually amounts to

.. code-block:: sh

    echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc
    source ~/.bashrc
