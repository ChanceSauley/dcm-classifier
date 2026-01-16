from pprint import pp
from dcm_classifier.dicom_series import DicomSingleSeries
from dcm_classifier.study_processing import ProcessOneDicomStudyToVolumesMappingBase
from dcm_classifier.image_type_inference import ImageTypeClassifierBase

my_inferer = ImageTypeClassifierBase()
test = ProcessOneDicomStudyToVolumesMappingBase(
    study_directory="/Users/csauley/Downloads/multi-frame-input", inferer=my_inferer
)

test.run_inference()

pp(test.series_dictionary)

x: DicomSingleSeries
for i, x in test.series_dictionary.items():
    tt = x.get_volume_list()[0]
    print(
        f"{tt.get_series_modality()} with Description {tt.get_dicom_field_by_name('SeriesDescription')}"
    )
