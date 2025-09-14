import cloudinary
import cloudinary.uploader
from fastapi import UploadFile

from src.config import settings

# Configure Cloudinary
cloudinary.config(
    cloud_name=settings.cloudinary_name,
    api_key=settings.cloudinary_api_key,
    api_secret=settings.cloudinary_api_secret,
    secure=True,
)


class CloudinaryService:

    @staticmethod
    def upload_image(file: UploadFile, folder: str = "avatars"):
        """Upload image to Cloudinary and return URL."""
        try:
            # Upload image
            result = cloudinary.uploader.upload(
                file.file,
                folder=folder,
                public_id=f"{folder}/{file.filename}",
                overwrite=True,
                resource_type="image",
                transformation=[
                    {"width": 250, "height": 250, "crop": "fill"},
                    {"quality": "auto"},
                ],
            )

            return result.get("secure_url")
        except Exception as e:
            print(f"Error uploading to Cloudinary: {e}")
            return None

    @staticmethod
    def get_url_for_avatar(public_id: str, version: str):
        """Generate URL for avatar with transformations."""
        return cloudinary.utils.cloudinary_url(
            public_id,
            version=version,
            crop="fill",
            width=250,
            height=250,
            quality="auto",
        )[0]


cloudinary_service = CloudinaryService()
