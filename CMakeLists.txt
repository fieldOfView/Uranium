project(uranium)

cmake_minimum_required(VERSION 2.8.12)

include(GNUInstallDirs)

find_package(PythonInterp 3.4.0 REQUIRED)

# Tests
add_custom_target(tests)
file(GLOB test_files tests/*/Test*.py)
foreach(file ${test_files})
    add_custom_command(TARGET tests POST_BUILD COMMAND "PYTHONPATH=${CMAKE_SOURCE_DIR}" ${PYTHON_EXECUTABLE} ARGS ${file} COMMENT "Running test ${file}")
endforeach()

# Benchmarks
add_custom_target(benchmark)
file(GLOB bench_files tests/benchmarks/*/profile*.py)
foreach(file ${bench_files})
    add_custom_command(TARGET benchmark POST_BUILD COMMAND "PYTHONPATH=${CMAKE_SOURCE_DIR}" kernprof ARGS -l -v ${file})
endforeach()

# Documentation
find_package(Doxygen)
if(${DOXYGEN_FOUND})
    add_custom_target(doc ${DOXYGEN_EXECUTABLE} ${CMAKE_SOURCE_DIR}/Doxyfile WORKING_DIRECTORY ${CMAKE_SOURCE_DIR})
endif()

# Extract Strings
add_custom_target(extract-messages ${CMAKE_SOURCE_DIR}/scripts/extract-messages ${CMAKE_SOURCE_DIR} uranium)

# Build Translations
find_package(Gettext)

if(GETTEXT_FOUND)
    # translations target will convert .po files into .mo and .qm as needed.
    # The files are checked for a _qt suffix and if it is found, converted to
    # qm, otherwise they are converted to .po.
    add_custom_target(translations ALL)
    # copy-translations can be used to copy the built translation files from the
    # build directory to the source resources directory. This is mostly a convenience
    # during development, normally you want to simply use the install target to install
    # the files along side the rest of the application.
    add_custom_target(copy-translations)

    #TODO: Properly install the built files. This should be done after we move the applications out of the Uranium repo.
    set(languages
        en
        x-test
        ru
        fr
        de
        it
        es
        fi
        pl
        cs
        bg
    )
    foreach(lang ${languages})
        file(GLOB po_files resources/i18n/${lang}/*.po)
        foreach(file ${po_files})
            string(REGEX REPLACE ".*/(.*).po" "${lang}/\\1.mo" mofile ${file})
            add_custom_command(TARGET translations POST_BUILD COMMAND mkdir ARGS -p ${lang} COMMAND ${GETTEXT_MSGFMT_EXECUTABLE} ARGS ${file} -o ${mofile})
        endforeach()

        file(GLOB mo_files ${CMAKE_BINARY_DIR}/${lang}/*.mo)
        foreach(file ${mo_files})
            add_custom_command(TARGET copy-translations POST_BUILD COMMAND cp ARGS ${file} ${CMAKE_SOURCE_DIR}/resources/i18n/${lang}/LC_MESSAGES COMMENT "Copying ${file}...")
        endforeach()

        install(FILES ${mo_files} DESTINATION ${CMAKE_INSTALL_DATADIR}/uranium/resources/i18n/${lang}/LC_MESSAGES/)
    endforeach()
endif()

if(APPLE OR WIN32)
    install(DIRECTORY UM DESTINATION lib/python${PYTHON_VERSION_MAJOR}.${PYTHON_VERSION_MINOR}/site-packages)
else()
    install(DIRECTORY UM DESTINATION lib/python${PYTHON_VERSION_MAJOR}/dist-packages)
endif()
install(DIRECTORY resources DESTINATION ${CMAKE_INSTALL_DATADIR}/uranium)
install(DIRECTORY plugins DESTINATION lib/uranium)

include(CPackConfig.cmake)
