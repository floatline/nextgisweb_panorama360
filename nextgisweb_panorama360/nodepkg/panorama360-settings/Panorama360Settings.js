import { FieldsForm, useForm} from "@nextgisweb/gui/fields-form";
import { useEffect, useState, useMemo } from "react";
import i18n from "@nextgisweb/pyramid/i18n!gui";
//{panorama_enabled, panorama_layer_field}
export const Panorama360Settings = ( {onChange, values} ) =>  {
    
    const form = useForm()[0];
    //const [values_, setValues_] = useState(values); - not needed
    // const [panoramaEnabled, setPanoramaEnabled] = useState(panorama_enabled);
    // const [panoramaLayerField, setPanoramaLayerField] = useState(panorama_layer_field);
    // // const [values, setValues] = useState();



    

    const fields =  [
        {
            name: "panorama_enabled",
            label: i18n.gettext("Enable Panorama360"),
            widget: "checkbox",
            required: true,
        
        },
        {
            name: "panorama_layer_field",
            label: i18n.gettext("Field name"),
            required: true,
            //disabled: !panorama_enabled,
            widget: "input"
        }
    ] 



    useEffect(() => { 
        //update form
        form.setFieldsValue(values);
        console.log("I'm in useEffect")
    }, [values]) 

    
    
    // const updateField()

    // const onEnabledChange = (val) => {
    //     setPanoramaEnabled(val);
    // };

    // const onFieldsChange = (val) => {
    //     setPanoramaLayerField(val);
    // }

    const onFieldsChange = (changedFields) => {
       console.log(...changedFields);
       console.log("I'm running onFieldsChange")
    };

    //const initVals = [true, null];
    return (
           <div className="ngw-panorama360-settings-form"
           style={{padding: "16px"}}>
            <h1>Panorama360 Settings</h1>
            <FieldsForm 
                fields={fields}
                form={form}
                onFieldsChange={onFieldsChange}
                initialValues={values}
                // onChange={ 
                //     ({ value })
                // }
            >
            </FieldsForm>
            </div>
    );
}



    
    



