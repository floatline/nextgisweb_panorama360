import { FieldsForm, useForm } from "@nextgisweb/gui/fields-form";
import { useEffect, useState, useMemo } from "react";
import i18n from "@nextgisweb/pyramid/i18n!gui";
export const Panorama360Settings = ({ onChange, values }) => {
  const form = useForm()[0];

  const fields = [
    {
      name: "enabled",
      label: i18n.gettext("Enable Panorama360"),
      widget: "checkbox",
      required: true,
    },
    {
      name: "panorama_layer_field",
      label: i18n.gettext("Field name"),
      required: true,
      widget: "input",
    },
  ];

  useEffect(() => {
    form.setFieldsValue(values);
  }, [values]);

  return (
    <div className="ngw-panorama360-settings-form" style={{ padding: "16px" }}>
      <h1>Panorama360 Settings</h1>
      <FieldsForm
        fields={fields}
        form={form}
        initialValues={values}
        onChange={async (v) => {
          if (await v.isValid()) {
            onChange(v.value);
          }
        }}
      ></FieldsForm>
    </div>
  );
};
