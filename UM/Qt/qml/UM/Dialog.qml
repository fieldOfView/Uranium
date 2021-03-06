// Copyright (c) 2015 Ultimaker B.V.
// Uranium is released under the terms of the AGPLv3 or higher.

import QtQuick 2.2
import QtQuick.Window 2.1
import QtQuick.Layouts 1.1

import UM 1.0 as UM

Window {
    id: base

    modality: Qt.ApplicationModal;
    flags: Qt.Dialog | Qt.CustomizeWindowHint | Qt.WindowTitleHint | Qt.WindowCloseButtonHint;

    width: Screen.devicePixelRatio * 640;
    height: Screen.devicePixelRatio * 480;

    property int margin: Screen.devicePixelRatio * 8;

    default property alias contents: contentItem.children;

    property alias leftButtons: leftButtonRow.children;
    property alias rightButtons: rightButtonRow.children;

    signal accepted();
    signal rejected();

    function accept() {
        base.visible = false;
        base.accepted();
    }

    function reject() {
        base.visible = false;
        base.rejected();
    }

    function open() {
        base.visible = true;
    }

    Rectangle {
        anchors.fill: parent;
        color: palette.window;

        focus: base.visible;

        Keys.onEscapePressed: base.reject();

        Item {
            id: contentItem;

            anchors {
                left: parent.left;
                leftMargin: base.margin;
                right: parent.right;
                rightMargin: base.margin;
                top: parent.top;
                topMargin: base.margin;
                bottom: buttonRow.top;
                bottomMargin: base.margin;
            }
        }

        Item {
            id: buttonRow;

            anchors {
                bottom: parent.bottom;
                bottomMargin: base.margin;
                left: parent.left;
                leftMargin: base.margin;
                right: parent.right;
                rightMargin: base.margin;
            }
            height: childrenRect.height;

            Row { id: leftButtonRow; anchors.left: parent.left; }

            Row { id: rightButtonRow; anchors.right: parent.right; }
        }
    }

    SystemPalette { id: palette; }
}
